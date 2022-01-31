#!/bin/env python3

import sys
from collections import defaultdict

fin = sys.stdin
fout = sys.stdout


def permutation(p1, p2):
    l1 = defaultdict(int)
    l2 = defaultdict(int)

    for letter in p1:
        l1[letter] += 1

    for letter in p2:
        l2[letter] += 1

    return l1 == l2


def solve():
    correct = False

    P = fin.readline().strip()
    H = fin.readline().strip()

    for i in range(len(H) - len(P) + 1):
        correct = correct or permutation(P, H[i:i + len(P)])
        if correct:
            break

    print("1" if correct else "0", file=fout)


def main():
    T = int(fin.readline().strip())
    for _ in range(T):
        solve()


if __name__ == "__main__":
    fin = open(input(), 'r')
    fout = open(input(), 'w')
    main()
