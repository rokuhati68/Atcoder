from heapq import heappop,heappush
N,M = map(int,input().split())
A = list(map(int,input().split()))
edge = [[]for _ in range(N)]
sumcost = [0] * N
for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
    sumcost[u] += A[v]
    sumcost[v] += A[u]

pq = []
for i in range(N):
    heappush(pq,(sumcost[i],-A[i],i))

ans = -1
s= set()
while pq:
    cost,a,now = heappop(pq)
    if now in s:
        continue
    ans = max(ans,cost)
    s.add(now)
    a *= -1
    for to in edge[now]:
        if to in s:
            continue
        sumcost[to] -= a
        heappush(pq,(sumcost[to],-A[to],to))

print(ans)
    