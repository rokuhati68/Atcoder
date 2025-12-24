from atcoder.dsu import DSU
N = int(input())
l = []
for _ in range(N - 1):
    u,v,w = map(int,input().split())
    l.append((w,u-1,v-1))
l.sort()
uf = DSU(N)
ans = 0
for i in range(N-1):
    w,u,v = l[i]
    ans += (w * (uf.size(u) * uf.size(v)))
    uf.merge(u,v)

print(ans)