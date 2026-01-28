from collections import deque
N,M,L,S,T = map(int,input().split())
edge = [[]for _ in range(N)]
for _ in range(M):
    u,v,c = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append((v,c))

ans = set()
q = deque()
q.append((0,0,0))
while q:
    now,cost,cnt = q.popleft()
    if cnt == L:
        if S <= cost <= T:
            ans.add(now + 1)
        continue
    if cost >= T:
        continue
    for to,add in edge[now]:
        if cost + add > T:
            continue
        q.append((to,cost + add,cnt + 1))

ans = list(ans)
ans.sort()
print(*ans)
