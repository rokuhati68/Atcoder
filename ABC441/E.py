from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum_prefix(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

def main():
    N = int(input())
    S = input().strip()

    P = [0] * (N + 1)
    for i, ch in enumerate(S, 1):
        if ch == 'A':
            P[i] = P[i-1] + 1
        elif ch == 'B':
            P[i] = P[i-1] - 1
        else:  
            P[i] = P[i-1]

    vals = sorted(set(P))
    def idx(x): return bisect_left(vals, x)
    print(P)
    fw = Fenwick(len(vals))
    ans = 0

    for x in P:
        print(fw.bit)
        k = idx(x)
        ans += fw.sum_prefix(k)  
        fw.add(k, 1)
        print(ans)
    print(ans)

if __name__ == "__main__":
    main()
