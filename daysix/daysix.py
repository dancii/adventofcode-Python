#/usr/bin/python

from collections import Counter
import operator

#Change from min to max to solve part 1

def main():
    jammed_messages = open('input.txt').read().strip().split('\n')
    first_col = []
    sec_col = []
    third_col = []
    fourth_col = []
    fifth_col = []
    sixth_col = []
    seventh_col = []
    eight_col = []

    answer = ""

    for jammed_message in jammed_messages:
        first_col.append(jammed_message[0])
        sec_col.append(jammed_message[1])
        third_col.append(jammed_message[2])
        fourth_col.append(jammed_message[3])
        fifth_col.append(jammed_message[4])
        sixth_col.append(jammed_message[5])
        seventh_col.append(jammed_message[6])
        eight_col.append(jammed_message[7])

    first_col_dict = Counter(first_col)
    sec_col_dict = Counter(sec_col)
    answer += min(Counter(first_col).iteritems(), key=operator.itemgetter(1))[0]
    answer += min(Counter(sec_col).iteritems(), key=operator.itemgetter(1))[0]
    answer += min(Counter(third_col).iteritems(), key=operator.itemgetter(1))[0]
    answer += min(Counter(fourth_col).iteritems(), key=operator.itemgetter(1))[0]
    answer += min(Counter(fifth_col).iteritems(), key=operator.itemgetter(1))[0]
    answer += min(Counter(sixth_col).iteritems(), key=operator.itemgetter(1))[0]
    answer += min(Counter(seventh_col).iteritems(), key=operator.itemgetter(1))[0]
    answer += min(Counter(eight_col).iteritems(), key=operator.itemgetter(1))[0]

    print(answer)

main()
