from collections import deque
def dfs(c, depth, dist):
    q = deque()
    q.append((c,depth))
    while q:
        now,cost = q.pop()
        dist[now] = cost
        for d in g[now]:
            if dist[d] != -1:
                continue
            q.append((d,cost + 1))
            


N = int(input())
g = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = [int(i) for i in input().split()]
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

d0 = [-1] * N
dfs(0, 0, d0)
u = max([(d0[i], i) for i in range(N)])[1]
du = [-1] * N
dfs(u, 0, du)
v = max([(du[i], i) for i in range(N)])[1]
dv = [-1] * N
dfs(v, 0, dv)

for i in range(N):
    print(max((du[i], u), (dv[i], v))[1] + 1)
