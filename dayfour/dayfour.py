#!/usr/bin/python
from collections import Counter
from collections import OrderedDict
from string import ascii_lowercase
import re
import string

rooms = open('input.txt').read().strip().split('\n')
alphabet = OrderedDict((ch, idx) for idx, ch in enumerate(ascii_lowercase, 0))

#USE FOR LATER
# print(dict_letters.get("a"))

def main():
    sector_id_to_decrypt = []
    sum_of_sector_ids = 0
    for room in rooms:
        all_the_letters = ""
        letters = room.split('-')

        for x in range(0,len(letters)-1):
            all_the_letters+=letters[x]

        dict_letters = Counter(all_the_letters)

        regex_for_checksum = re.search(r"\[([A-Za-z]+)\]", letters[len(letters)-1])
        checksum = list(regex_for_checksum.group(1))

        all_in_order = True
        for x in range(0, len(checksum)-1):
            all_in_order = is_greater_then_next_or_alphabetical_order(dict_letters, checksum[x], checksum[x+1])
            if all_in_order == False:
                break;
        if all_in_order == True:
            regex_for_sector_id = re.search(r"(.*?)\s*\[",letters[len(letters)-1])
            sector_id = regex_for_sector_id.group(1)
            sum_of_sector_ids+=int(sector_id)
            prepare_for_caesar_cypher(letters, sector_id)
            sector_id_to_decrypt.append(sector_id)
    print('Sum of sector ids', sum_of_sector_ids)

def is_greater_then_next_or_alphabetical_order(dict_letters, A_key, B_key):
    try:
        a_value = int(dict_letters.get(A_key))
        b_value = int(dict_letters.get(B_key))
    except TypeError:
        return False

    if a_value > b_value:
        return True
    elif a_value == b_value:
        return is_alphabetical_order(A_key, B_key)
    else:
        return False

def is_alphabetical_order(a_value, b_value):
    temp_list = []
    temp_list.append(a_value)
    temp_list.append(b_value)
    temp_list = sorted(temp_list)

    if temp_list[0] == a_value:
        return True
    else:
        return False


def prepare_for_caesar_cypher(sentence, shift):
    decrypted_sentence = ""
    del sentence[-1]
    for word in sentence:
        decrypted_word = ""
        for letter in word:
            decrypted_word += caesar_cypher(letter, shift)
        decrypted_sentence+=decrypted_word+" "
    if "north" in decrypted_sentence:
        print("North pole storage id: ",shift)


def caesar_cypher(letter, shift):
    x = int(alphabet.get(letter))
    new_position = ((x+int(shift)) % 26);
    new_letter = alphabet.keys()[alphabet.values().index(new_position)]
    return new_letter
main()
