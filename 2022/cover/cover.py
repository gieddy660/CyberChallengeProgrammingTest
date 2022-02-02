#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
fin = sys.stdin  # File di input fornito dalla piattaforma
fout = sys.stdout  # File di output fornito dalla piattaforma


def conta(N, K, ranges):
    # SCRIVI QUA IL TUO CODICE
    return 0


if __name__ == '__main__':
    f_name = input()
    fin = open(f_name + '.txt', 'r')
    fout = open(f_name + '_out.txt', 'w')
    N, K = map(int, fin.readline().strip().split(" "))
    ranges = []

    for _ in range(N):
        start, end = map(int, fin.readline().strip().split(" "))
        ranges.append([start, end])

    print(conta(N, K, ranges), file=fout)
