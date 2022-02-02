#!/bin/env python3

import sys
import string

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # Output da inviare alla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
# fin = sys.stdin  # input fornito dalla piattaforma
# fout = sys.stdout  # Output da inviare alla piattaforma


def controlla(nuova, vecchia):

    if not 8 <= len(nuova) <= 16:
        return 0

    if len(vecchia) + 1 == len(nuova):
        for i in range(len(nuova)):
            if vecchia == nuova[:i] + nuova[i + 1:]:
                return 0
    elif len(vecchia) == len(nuova):
        for i in range(len(nuova)):
            if vecchia[:i] + vecchia[i + 1:] == nuova[:i] + nuova[i + 1:]:
                return 0
    elif len(vecchia) - 1 == len(nuova):
        for i in range(len(vecchia)):
            if vecchia[:i] + vecchia[i + 1:] == nuova:
                return 0

    prev_char = None
    upper = False
    lower = False
    digit = False
    special = False
    for char in nuova:
        if char == prev_char:
            return 0
        upper = upper or (char in string.ascii_uppercase)
        lower = lower or (char in string.ascii_lowercase)
        digit = digit or (char in string.digits)
        special = special or (char in string.punctuation)
        prev_char = char

    return 1 if upper and lower and digit and special else 0


if __name__ == '__main__':
    f_name = input()
    fin = open(f_name + '.txt', 'r')
    fout = open(f_name + '_out.txt', 'w')
    N = int(fin.readline().strip())

    for _ in range(N):
        nuova, vecchia = fin.readline().strip().split(" ")
        print(controlla(nuova, vecchia), file=fout)
