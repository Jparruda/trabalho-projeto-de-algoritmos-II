#!/bin/python3

import math
import os
import random
import re
import sys
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def checkMagazine(magazine, note):
    magazine_count = {}
    for word in magazine:
        word = remove_accents(word)
        magazine_count[word] = magazine_count.get(word, 0) + 1

    for word in note:
        word = remove_accents(word)
        if word in magazine_count and magazine_count[word] > 0:
            magazine_count[word] -= 1
        else:
            print("No")
            return

    print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()
    note = input().rstrip().split()

    checkMagazine(magazine, note)
