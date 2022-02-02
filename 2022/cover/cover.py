#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
# fin = sys.stdin  # File di input fornito dalla piattaforma
# fout = sys.stdout  # File di output fornito dalla piattaforma


def conta(N, K, ranges):
    if K > N:
        return 0

    minim = min((r[0]) for r in ranges)
    maxim = max((r[1]) for r in ranges)

    auxiliary = {range(minim, maxim): 0}

    for start, end in ranges:
        new_auxiliary = dict()
        for r, val in auxiliary.items():
            if start in r and (end - 1) in r:
                if range(r.start, start):
                    new_auxiliary[range(r.start, start)] = val
                if val + 1 <= K:
                    new_auxiliary[range(start, end)] = val + 1
                if range(end, r.stop):
                    new_auxiliary[range(end, r.stop)] = val

            elif start in r:
                if range(r.start, start):
                    new_auxiliary[range(r.start, start)] = val
                if val + 1 <= K:
                    new_auxiliary[range(start, r.stop)] = val + 1

            elif (end - 1) in r:
                if val + 1 <= K:
                    new_auxiliary[range(r.start, end)] = val + 1
                if range(end, r.stop):
                    new_auxiliary[range(end, r.stop)] = val

            elif r.start in range(start, end) and r.stop in range(start, end):
                if val + 1 <= K:
                    new_auxiliary[r] = val + 1

            else:
                new_auxiliary[r] = val

        auxiliary = new_auxiliary

    res = 0
    for r, val in auxiliary.items():
        if val == K:
            res += len(r)

    return res


if __name__ == '__main__':
    f_name = input()
    fin = open(f_name + '.txt', 'r')
    fout = open(f_name + '_out.txt', 'w')
    N, K = map(int, fin.readline().strip().split(" "))
    ranges = []

    for _ in range(N):
        start, end = map(int, fin.readline().strip().split(" "))
        ranges.append([start, end + 1])

    print(conta(N, K, ranges), file=fout)
