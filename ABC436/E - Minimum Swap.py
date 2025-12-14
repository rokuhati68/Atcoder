from atcoder.dsu import DSU
N = int(input())
P = list(map(int,input().split()))
uf = DSU(N)
for i in range(N):
    p = P[i] - 1
    uf.merge(i,p)

ans = 0
for g in uf.groups():
    _len = len(g)
    ans += _len *(_len - 1)

print(ans // 2)