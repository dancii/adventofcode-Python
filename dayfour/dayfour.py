#!/usr/bin/python
from collections import Counter

rooms = open('input.txt').read().strip().split('\n')

def main():
    for room in rooms:
        all_the_letters = ""
        letters = room.split('-')
        for x in range(0,len(letters)-1):
            all_the_letters+=letters[x]
        print(Counter(all_the_letters))

main()
