from collections import deque
N = int(input())
edge = [[]for _ in range(N)]
for _ in range(N - 1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

def dfs(root):
    dist = [-1] * N
    dist[root] = 0
    q = deque()
    q.append(root)
    while q:
        now = q.pop()
        orderq.append(now)
        for to in edge[now]:
            if dist[to] != -1:
                continue
            dist[to] = dist[now] + 1
            q.append(to)
    return dist

orderq = deque()
dist = dfs(0)
ans = [-1] * N
ans[0] = dist[0]

