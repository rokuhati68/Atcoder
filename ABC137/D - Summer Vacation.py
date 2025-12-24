from heapq import heappush,heappop
N, M = map(int,input().split())
nonCand = []
for _ in range(N):
    a,b = map(int,input().split())
    heappush(nonCand,(a,-b))

heappush(nonCand,(10**10,0))
ans = 0
cand = []

for i in range(1,M + 1):
    
    while True:
        a,b = heappop(nonCand)
        if a <= i:
            heappush(cand,b)
        else:
            heappush(nonCand,(a,b))
            break
    if len(cand) > 0:
        value = heappop(cand)
        ans += -value

print(ans)
