#/usr/bin/python

import re

def main():
    compressed_text = open('input.txt').read().strip().split('\n')

    for line in compressed_text:
        inside_para = re.findall('\(([^\)]+)\)', line)
        outside_para = re.findall('(.*?)\(.*?\)', line)
        print(outside_para)

main()
