from collections import deque

H,W = map(int,input().split())
S = [list(input())for _ in range(H)]
a,b,c,d = map(int,input().split())
a -= 1
b -= 1
c -= 1
d -= 1
dist = [[10**10] * W for _ in range(H)]
dist[a][b] = 0

dxy = [(0,1),(1,0),(-1,0),(0,-1)]
q= deque()
q.append((a,b,0))
while q:
    ny,nx,cost = q.popleft()
    if dist[ny][nx] < cost:
        continue
    for dy, dx in dxy:
        ty = ny + dy
        tx = nx + dx
        if 0 <= ty < H and 0 <= tx < W:
            if S[ty][tx] == "." and dist[ty][tx] > cost:
                dist[ty][tx] = cost
                q.appendleft((ty,tx,cost))
            if S[ty][tx] == "#" and dist[ty][tx] > cost + 1:
                dist[ty][tx] = cost + 1
                q.append((ty,tx,cost + 1))
            ty += dy
            tx += dx
            if 0 <= ty < H and 0 <= tx < W:
                if dist[ty][tx] > cost + 1:
                    dist[ty][tx] = cost + 1
                    q.append((ty,tx,cost + 1))

print(dist[c][d])
