from atcoder.dsu import DSU
from collections import deque
N, M = map(int,input().split())
edge =[set()for _ in range(N)]
revedge = [set()for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    if a < b:
        a, b = b, a
    edge[a].add(b)
    revedge[b].add(a)


ans = {0}
uf = DSU(N + 1)
uf2 = DSU(N + 1)
for i in range(N):
    for to in edge[i]:
        uf.merge(i,to)
    for to in revedge[i]:
        uf2.merge(i,to)
    if uf.size(0) == i + 1:
        print(uf2.size(0) - i - 1)
    else:
        print(-1)
        