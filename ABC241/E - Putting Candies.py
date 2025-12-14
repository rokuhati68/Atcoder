N, K = map(int,input().split())
A = list(map(int,input().split()))
dp = [[-1] * N for _ in range(46)]
_sum = [[0] * N for _ in range(46)]
for i in range(N):
    to = (i +A[i]) % N
    dp[0][i] = to
    _sum[0][i] += A[i]
    
for i in range(45):
    for j in range(N):
        dp[i + 1][j] = dp[i][dp[i][j]]

for i in range(45):
    for j in range(N):
        _sum[i + 1][j] += _sum[i][j]
        _sum[i + 1][j] += _sum[i][dp[i][j]]

ans = 0
now = 0
for i in range(45):
    if K >> i & 1 == 1:
        ans += _sum[i][now]
        now = dp[i][now]

print(ans)

    