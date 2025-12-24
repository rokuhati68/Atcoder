from collections import deque

N, M = map(int, input().split())
e = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    e[u].append(v)
    e[v].append(u)

s = input().strip()

# f[v][0], f[v][1] : その頂点に到達した始点SのID（異なる2つ）
# d[v][0], d[v][1] : それぞれの距離
f = [[-1, -1] for _ in range(N)]
d = [[-1, -1] for _ in range(N)]

q = deque()

for i in range(N):
    if s[i] == 'S':
        f[i][0] = i
        d[i][0] = 0
        q.append((i, i, 0))  # (start_id, node, dist)

while q:
    start_id, v, dist = q.popleft()
    nd = dist + 1
    for to in e[v]:
        if f[to][0] == -1:
            f[to][0] = start_id
            d[to][0] = nd
            q.append((start_id, to, nd))
        elif f[to][1] == -1 and f[to][0] != start_id:
            f[to][1] = start_id
            d[to][1] = nd
            q.append((start_id, to, nd))

for i in range(N):
    if s[i] == 'D':
        print(d[i][0] + d[i][1])
