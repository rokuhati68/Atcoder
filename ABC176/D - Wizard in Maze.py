from heapq import heappop,heappush
H, W = map(int,input().split())
Ch,Cw = map(int,input().split())
Dh,Dw = map(int,input().split())
Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1
S = [input()for _ in range(H)]

dist = [[10**10]*W for _ in range(H)]
dist[Ch][Cw] = 0
pq = []
heappush(pq,(0,Ch,Cw))
while pq:
    cost,ny,nx = heappop(pq)
    if dist[ny][nx] < cost:
        continue
    for dy, dx in ((1,0),(0,1),(-1,0),(0,-1)):
        ty = ny + dy
        tx = nx + dx
        if 0 <= ty < H and 0 <= tx < W and S[ty][tx] == ".":
            if dist[ty][tx] > cost:
                dist[ty][tx] = cost
                heappush(pq,(cost,ty,tx))
    for dy in range(-2, 3):
        ty = ny + dy
        if 0 <= ty < H:
            for dx in range(-2, 3):
                tx = nx + dx
                if 0 <= tx < W and S[ty][tx] == ".":
                    if dist[ty][tx] > cost + 1:
                        dist[ty][tx] = cost + 1
                        heappush(pq,(cost + 1,ty,tx))

if dist[Dh][Dw] == 10 ** 10:
    print(-1)
else:
    print(dist[Dh][Dw])

