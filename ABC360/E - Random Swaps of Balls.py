N, K = map(int,input().split())
dp = [0] * (K + 1)
dp[0] = 1
MOD = 998244353
p = ((N - 1) * (N - 1) + 1) * pow(N * N, MOD - 2, MOD) % MOD
q = 2 * pow(N * N, MOD - 2, MOD) % MOD

for i in range(K):
    dp[i + 1] = dp[i] * p + (1 - dp[i]) * q
    dp[i + 1] %= MOD

ans = dp[-1]
ans += (((N * (N + 1) // 2) - 1) * (1 - dp[-1]) * pow(N - 1, MOD - 2, MOD))%MOD
print(ans%MOD)