#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # Output da inviare alla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
# fin = sys.stdin  # input fornito dalla piattaforma
# fout = sys.stdout  # Output da inviare alla piattaforma
from collections import defaultdict


def swap(N, V):
    # stuff = defaultdict(int)
    # for num in V:
    #     stuff[num] += 1
    #
    # auxilary = list(stuff)
    #
    # for i in range(1, N - 1):
    #     if V[i] > V[i + 1] >= V[i - 1]:
    #         print(V[i])
    #         if V[i - 1] == V[i + 1]:
    #
    #         return abs(sorted(V).index(V[i]) - i)
    #     elif V[i] < V[i - 1] <= V[i + 1]:
    #         print(V[i])
    #         return abs((N - 1 - sorted(V, reverse=True).index(V[i])) - i)

    # if V[N-1] < V[N-2]:
    #     return abs((N - 1 - sorted(V, reverse=True).index(V[N-1])) - N - 1)
    # elif V[0] > V[1]:
    #     return abs(sorted(V).index(V[0]) - 0)
    t = None
    d = ''
    for i in range(N):
        if i == 0:
            if V[i] > V[i + 1]:
                d = 'growing'
                t = i
        elif i == N - 1:
            if V[i] < V[i - 1]:
                d = 'shrinking'
                t = i
        else:
            if V[i] > V[i + 1] >= V[i - 1]:
                d = 'growing'
                t = i
            elif V[i] < V[i - 1] <= V[i + 1]:
                d = 'shrinking'
                t = i
    print(t, d)
    counter = 0
    n = V[t]
    t += (1 if d == 'growing' else - 1)
    while d == 'growing' and V[t] < n:
        counter += 1 if V[t + 1] > V[t] else 0
        t += 1
    while d == 'shrinking' and V[t] > n:
        counter += 1 if V[t - 1] < V[t] else 0
        t -= 1
    return counter


if __name__ == '__main__':
    f_name = input()
    fin = open(f_name + '.txt', 'r')
    fout = open(f_name + '_out.txt', 'w')
    N = int(fin.readline().strip())
    V = list(map(int, fin.readline().strip().split(" ")))
    print(swap(N, V), file=fout)
