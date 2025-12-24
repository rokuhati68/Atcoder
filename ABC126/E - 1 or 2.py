from atcoder.dsu import DSU
N, M = map(int,input().split())
uf = DSU(N)
for _ in range(M):
    x,y,z = map(int,input().split())
    x -= 1
    y -= 1
    uf.merge(x,y)

print(len(uf.groups()))