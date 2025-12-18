from heapq import heappop,heappush
N, M = map(int,input().split())
pq = []
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    heappush(pq,(a, -b))

ans = 0
left = -1
right = 10**10
while pq:
    l,r = heappop(pq)
    r *= -1
    if l >= right:
        ans += 1
        left = l
        right = r
    else:
        left = max(left,l)
        right = min(right,r)

ans += 1
print(ans)
