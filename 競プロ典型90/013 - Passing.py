from heapq import heappop,heappush

N, M = map(int,input().split())
edge = [[]for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append((b,c))
    edge[b].append((a,c))

def djkstra(st):
    q = []
    dist = [10**10] * N
    dist[st] = 0
    heappush(q,(0,st))
    while q:
        cost,now = heappop(q)
        if dist[now] < cost:
            continue
        for to, add in edge[now]:
            if dist[to] > cost + add:
                dist[to] = cost + add
                heappush(q,(cost + add, to))

    return dist

dist1 = djkstra(0)
dist2 = djkstra(N - 1)
for i in range(N):
    print(dist1[i] + dist2[i])
    
    
    
    
    
    
    