N, K = map(int,input().split())
X = list(map(int,input().split()))
A = list(map(int,input().split()))
dp = [[-1] * N for _ in range(60)]

for i in range(N):
    x = X[i] - 1
    dp[0][i] = x
for i in range(59):
    for j in range(N):
        dp[i + 1][j] = dp[i][dp[i][j]]

ans = []
for x in range(N):
    for i in range(60):
        if K >> i & 1 == 1:
            x = dp[i][x]
    ans.append(A[x])

print(*ans)