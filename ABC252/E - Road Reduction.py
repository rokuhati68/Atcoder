from heapq import heappop,heappush
N, M = map(int,input().split())
edge =[[]for _ in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append((b,c,i + 1))
    edge[b].append((a,c,i + 1))

dist = [10**30] * N
dist[0] = 0
ans = [-1] * N
pq = []
heappush(pq,(0,0))
while pq:
    cost,now = heappop(pq)
    if cost > dist[now]:
        continue
    for to,add,i in edge[now]:
        if dist[to] > cost + add:
            dist[to] = cost + add
            heappush(pq,(cost + add,to))
            ans[to] = i

print(*ans[1:])