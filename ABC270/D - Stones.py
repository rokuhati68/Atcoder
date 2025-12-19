N, K = map(int,input().split())
A = list(map(int,input().split()))

dp = [0 for _ in range(N + 1)]
for i in range(N + 1):
    for a in A:
        if a > i:
            break
        dp[i] = max(dp[i],i - dp[i - a])

print(dp[N])