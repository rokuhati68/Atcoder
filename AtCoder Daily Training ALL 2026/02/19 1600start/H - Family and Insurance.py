from collections import deque
N, M = map(int,input().split())
P = list(map(int,input().split()))
edge = [[] for _ in range(N)]
for i in range(N - 1):
    parent = P[i] - 1
    edge[parent].append(i + 1)

aft = [0] * N
for _ in range(M):
    x,y = map(int,input().split())
    x -= 1
    aft[x] = max(aft[x],y)


Flag = [False] * N
for i in range(N):
    if Flag[i]:
        continue
    if aft[i] == 0:
        continue
    q = deque([])
    q.append((i,aft[i]))
    while q:
        now,cnt = q.popleft()
        
        Flag[now] = True
        if cnt == 0:
            continue
        for to in edge[now]:
            if Flag[to]:
                continue
            q.append((to,max(cnt - 1,aft[to])))

        
print(sum(Flag))