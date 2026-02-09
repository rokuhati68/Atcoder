from heapq import heappush,heappop
N, T = map(int,input().split())
A = list(map(int,input().split()))
isOpen = True
pq = []
for a in A:
    heappush(pq,(a,0))

ans = 0
startTime = 0
while pq:
    time,id = heappop(pq)
    if time > T:
        continue
    if id == 1:
        isOpen = True
        startTime = time
    else:
        if isOpen:
            ans += time - startTime
            isOpen = False
            heappush(pq,(time + 100,1))
            preTime = time
if isOpen:
    ans += T - startTime      

print(ans)