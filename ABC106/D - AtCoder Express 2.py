N, M , Q = map(int,input().split())
ans = [[0] * (N + 1)for _ in range(N + 1)]
for _ in range(M):
    l,r = map(int,input().split())
    for i in range(l):
        ans[i][r - 1] += 1
        ans[i][N] -= 1

for i in range(N):
    for j in range(N):
        ans[i][j + 1] += ans[i][j]

for _ in range(Q):
    p,q = map(int,input().split())
    print(ans[p - 1][q - 1])