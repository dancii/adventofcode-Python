#!/usr/bin/python

import re

def main():
    ips = open('input.txt').read().strip().split('\n')

    ip_count = 0
    for ip in ips:
        #print(ip)
        #print('Inside brackets', len(inside_brackets))
        inside_brackets = re.findall(r"\[(\w+)\]", ip)
        if four_char_seq_inside(inside_brackets) == True:
            continue


        outside_brackets_regex_list = re.findall(r'[^[]+(?=\[[^]]*]|$)', ip)
        outside_brackets = []
        for string_outside_brackets_unsorted in outside_brackets_regex_list:
            try:
                outside_brackets.append(string_outside_brackets_unsorted.split(']')[1])
            except IndexError:
                outside_brackets.append(string_outside_brackets_unsorted.split(']')[0])

        if four_char_seq_outside(outside_brackets) == True:
            ip_count+=1

    print ip_count

def four_char_seq_inside(char_seqs):
    for char_seq in char_seqs:
        for x in range(0, len(char_seq)-3):
            first_part = char_seq[x] + char_seq[x+1]
            sec_part = char_seq[x+2] + char_seq[x+3]
            if first_part == sec_part[::-1]:
                if first_part == sec_part:
                    return False
                #print(first_part, sec_part)
                return True

def four_char_seq_outside(char_seqs):
    for char_seq in char_seqs:
        for x in range(0, len(char_seq)-3):
            first_part = char_seq[x] + char_seq[x+1]
            sec_part = char_seq[x+2] + char_seq[x+3]
            if first_part == sec_part[::-1]:
                if first_part == sec_part:
                    print(first_part, sec_part)
                    return False
                return True

def main2():
    ips = open('input.txt').read().strip().split('\n')

    ip_count = 0
    for ip in ips:
        outside_brackets_regex_list = re.findall(r'[^[]+(?=\[[^]]*]|$)', ip)
        outside_brackets = []
        for string_outside_brackets_unsorted in outside_brackets_regex_list:
            try:
                outside_brackets.append(string_outside_brackets_unsorted.split(']')[1])
            except IndexError:
                outside_brackets.append(string_outside_brackets_unsorted.split(']')[0])
        abas = ssl_outside(outside_brackets)
        if abas == False:
            continue
        else:
            inside_brackets = re.findall(r"\[(\w+)\]", ip)
            if ssl_inside(inside_brackets, abas) == True:
                ip_count+=1

    print ip_count

def ssl_outside(char_seqs):
    abas = []
    for char_seq in char_seqs:
        for x in range(0, len(char_seq)-2):
            aba_text = char_seq[x]+char_seq[x+1]+char_seq[x+2]
            if aba_text == aba_text[::-1]:
                if aba_text == len(aba_text) * aba_text[0]:
                    continue
                abas.append(aba_text)
    if len(abas) > 0:
        return abas
    return False

def ssl_inside(char_seqs, abas):
    for char_seq in char_seqs:
        for x in range(0, len(char_seq)-2):
            bab_text = char_seq[x]+char_seq[x+1]+char_seq[x+2]
            for aba in abas:
                if check_aba_bab(aba, bab_text) == True:
                    return True
    return False

def check_aba_bab(aba,bab):
    if aba[0] == bab[1] and aba[1] == bab[0] and aba[1] == bab[2]:
        #print('True',aba, bab)
        return True
    else:
        #print('False',aba, bab)
        return False

main2()
