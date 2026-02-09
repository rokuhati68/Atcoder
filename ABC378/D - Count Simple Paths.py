


def dfs(ny,nx,cnt):
    global ans
    if cnt == K:
        ans += 1
        return
    for dy, dx in ((1,0),(0,1),(-1,0),(0,-1)):
        ty = ny + dy
        tx = nx + dx
        idx = ty * W + tx
        if 0 <= ty < H and 0 <= tx < W:
            if S[ty][tx] == "#":
                continue
            if visited[idx]:
                visited[idx] = False
                dfs(ty,tx,cnt + 1)
                visited[idx] = True
                
H, W, K = map(int,input().split())
S =[input().strip()for _ in range(H)]

ans = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            visited = [True] * (H * W)
            visited[i * W + j] = False
            dfs(i,j,0)

print(ans)