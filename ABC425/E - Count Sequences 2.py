T, M = map(int,input().split())
    
dp = [[0]*5001 for _ in range(5001)]
dp[0][0] = 1
for n in range(1,5001):
    dp[n][0] = 1
    for k in range(1,n + 1):
        dp[n][k] = (dp[n - 1][k - 1] + dp[n - 1][k])%M

for _ in range(T):
    N = int(input())
    C = list(map(int,input().split()))
    _sum = sum(C)
    ans = 1
    for i in range(N):
        ans *= dp[_sum][C[i]]
        ans %= M
        _sum -= C[i]
    print(ans)
