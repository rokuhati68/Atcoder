from atcoder.dsu import DSU
from collections import deque
N,M = map(int,input().split())
edge = [[]for _ in range(N)]
uf = DSU(N)
for _ in range(M):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append((v,w))
    edge[v].append((u,-w))
    uf.merge(u,v)

visited = [True] * N
ans = [0] * N
for g in uf.groups():
    q = deque()
    leader = g[0]
    q.append(leader)
    ans[leader] = 0
    visited[leader] = False
    while q:
        now = q.popleft()
        for to,add in edge[now]:
            if visited[to]:
                visited[to] = False
                ans[to] = ans[now] + add
                q.append(to)

print(*ans)