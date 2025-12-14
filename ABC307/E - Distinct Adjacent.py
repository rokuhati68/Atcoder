N, M = map(int,input().split())
MOD = 998244353
dp = [[0,0]for _ in range(N)]
dp[0][0] = M
for i in range(N - 1):
    dp[i + 1][0] = dp[i][1]
    dp[i + 1][1] = (M - 1) * dp[i][0] + (M - 2) * dp[i][1]
    dp[i + 1][0] %= MOD
    dp[i + 1][1] %= MOD

print(dp[-1][1])