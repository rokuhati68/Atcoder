from collections import defaultdict
from heapq import heappop, heappush
N, M , K = map(int,input().split())
A = list(map(int,input().split()))
edge = [[]for _ in range(N)]
dic = defaultdict()
for i in range(N - 1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
    dic[(min(u,v),max(u,v))] = i

cnt = [0] * (N - 1)
for i in range(M -1):
    pq = []
    dist = [10**10] * N
    dist[A[i] - 1] = 0
    heappush(pq,(0,A[i] -1,-1))
    rev = [-1] * N
    while pq:
        cost,now,pre = heappop(pq)
        if dist[now] < cost:
            continue
        for to in edge[now]:
            if dist[to] > cost + 1:
                rev[to] = now
                dist[to] = cost + 1
                heappush(pq,(cost + 1,to,now))
    
    now = A[i + 1] - 1
    while now != -1:
        pre = rev[now]
        if pre == -1:
            break
        id = dic[(min(now,pre),max(now,pre))]
        cnt[id] += 1
        now = pre

_all = sum(cnt)
if _all<K or (_all-K)%2 == 1:
    print(0)
    exit()
dp = [0]*(10**5+1)
dp[0] = 1
MOD = 998244353
for i in range(N - 1):
    now_look = cnt[i]
    for j in reversed(range(10**5+1)):
        if now_look+j<=_all:
            dp[now_look+j] += dp[j]
            dp[now_look+j] %= MOD
#print(dp)
print(dp[(_all-K)//2]%MOD)