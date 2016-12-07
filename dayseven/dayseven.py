#!/usr/bin/python

import re

def main():
    ips = open('input.txt').read().strip().split('\n')

    ip_count = 0
    for ip in ips:
        print(ip)
        inside_brackets = re.findall(r"\[(\w+)\]", ip)
        print('Inside brackets', len(inside_brackets))

        if four_char_seq_inside(inside_brackets) == True:
            continue

        outside_brackets = re.findall(r'(.*?)\[.*?\]', ip)
        print('Outside brackets', outside_brackets)
        if four_char_seq_outside(outside_brackets) == True:
            ip_count+=1

    print ip_count

def four_char_seq_inside(char_seqs):
    for char_seq in char_seqs:
        for x in range(0, len(char_seq)-3):
            first_part = char_seq[x] + char_seq[x+1]
            sec_part = char_seq[x+2] + char_seq[x+3]
            if first_part[0] == sec_part[0]:
                return True
            if first_part == sec_part[::-1]:
                return True

def four_char_seq_outside(char_seqs):
    for char_seq in char_seqs:
        for x in range(0, len(char_seq)-3):
            first_part = char_seq[x] + char_seq[x+1]
            sec_part = char_seq[x+2] + char_seq[x+3]
            if first_part[0] == sec_part[0]:
                return False
            if first_part == sec_part[::-1]:
                return True

main()
