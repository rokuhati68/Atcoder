from heapq import heappop,heappush
N, M = map(int,input().split())
edge = [[]for _ in range(N)]
reveedge = [[]for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append((b,c))
    reveedge[b].append((a,c))

for i in range(N):
    pq = []
    pq.append((0,i))
    dist = [10 ** 10]*N
    dist[i] = 0
    while pq:
        cost,now = heappop(pq)
        for to, add in edge[now]:
            if dist[to] > cost + add:
                dist[to] = cost + add
                heappush(pq,(cost + add, to))
    
    ans = 10**10
    for to,add in reveedge[i]:
        ans = min(ans,dist[to] + add)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)