from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
ans = -m
for i in range(n):
    seen = [False]*n
    seen[i] = True
    q = deque([i])
    while q:
        v1 = q.popleft()
        for v2 in g[v1]:
            if not seen[v2]:
                seen[v2] = True
                q.append(v2)
    ans += sum(seen) - 1
print(ans)