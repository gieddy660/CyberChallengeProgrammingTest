#!/bin/env python3

import sys

fin = sys.stdin
fout = sys.stdout


def main():

    (N, K) = map(int, fin.readline().strip().split())
    V = list(map(int, fin.readline().strip().split()))

    # WRITE YOUR SOLUTION HERE
    solution = sum(sorted(V, reverse=True)[:K + 1])
    
    print(solution, file=fout)


if __name__ == "__main__":
    fin = open((t := input()) + '.txt', 'r')
    fout = open(t + '_out' + '.txt', 'w')
    main()
