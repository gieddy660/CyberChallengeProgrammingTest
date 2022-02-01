def main():
    n, k = map(int, fin.readline().strip().split())
    pols = list(map(int, fin.readline().strip().split()))
    res = sum(a * (2 ** i) for i, a in enumerate(pols))

    h = 0
    for i in range(n):
        if res % 2 ** i:
            continue
        b = (-res / 2 ** i) + pols[i]
        if abs(b) <= k:
            h += 1
    print(h, file=fout)


if __name__ == '__main__':
    fin = open(input(), 'r')
    fout = open(input(), 'w')
    main()