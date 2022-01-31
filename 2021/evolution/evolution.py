#!/bin/env python3

import sys


def solve(fin, fout):

    (N, M, K) = map(int, fin.readline().strip().split())

    G = []
    for _ in range(N):
        G.append(list(fin.readline().strip()))

    converted_G = []
    for row in G:
        converted_row = []
        for elem in row:
            if elem == '.':
                converted_row.append(0)
            elif elem == '+':
                converted_row.append(1)
            elif elem == '*':
                converted_row.append(-1)
        converted_G.append(converted_row)
    G = converted_G

    # WRITE HERE YOUR SOLUTION
    for _ in range(K):
        next_G = []
        t = ((-1, -1), (-1, 0), (-1, 1),
             (0, -1),           (0, 1),
             (1, -1),  (1, 0),  (1, 1))
        for h, row in enumerate(G):
            next_row = []
            for x, elem in enumerate(row):
                neighbours = 0
                for index, (dh, dx) in enumerate(t):
                    h_ = h + dh
                    x_ = x + dx
                    if h_ < 0 or h_ >= len(G):
                        continue
                    if x_ < 0 or x_ >= len(row):
                        continue
                    neighbours += abs(G[h_][x_])
                next_elem = elem
                if neighbours < 4:
                    next_elem = 0
                elif neighbours > 4 and elem == 0:
                    next_elem = 1
                elif neighbours > 4 and elem == 1:
                    next_elem = -1
                elif neighbours > 4 and elem == -1:
                    next_elem = 1
                next_row.append(next_elem)
            next_G.append(next_row)
        G = next_G

    converted_G = []
    for row in G:
        converted_row = []
        for elem in row:
            if elem == 0:
                converted_row.append('.')
            elif elem == 1:
                converted_row.append('+')
            elif elem == -1:
                converted_row.append('*')
        converted_G.append(converted_row)
    G = converted_G

    for r in G:
        print("".join(r), file=fout)


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
