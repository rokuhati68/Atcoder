from heapq import heappop,heappush
N = int(input())
a,b = map(int,input().split())
a -= 1
b -= 1
M = int(input())
edge = [[]for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    edge[x].append(y)
    edge[y].append(x)

pq = []
heappush(pq,(0,a))
dist = [10**10] * N
dist[a] = 0
cnt = [0] * N
cnt[a] = 1
MOD = 10**9 + 7
while pq:
    cost, now = heappop(pq)
    if dist[now] < cost:
        continue
    for to in edge[now]:
        if dist[to] < cost + 1:
            continue
        elif dist[to] == cost + 1:
            cnt[to] += cnt[now]
            cnt[to] %= MOD
        elif dist[to] > cost + 1:
            dist[to] = cost + 1
            cnt[to] = cnt[now]
            heappush(pq,(cost + 1,to))

print(cnt[b])
