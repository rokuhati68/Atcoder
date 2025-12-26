mod = 998244353
dp = [ [ 0 for _ in range(61)] for _ in range(61) ]
dp[1][1] = 1
import math
for i in range(2,61):
    t = 2 ** (i-1)
    for j in range(60):
        dp[i][j] = dp[i-1][j]
        if dp[i-1][j-1] != 0 or j == 1:
            dp[i][j] += dp[i-1][j-1] + t * math.comb(i-1,j-1)
            dp[i][j] %= mod
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    T = 0
    ans = 0
    x = 0
    for i in range(59,-1,-1):
        if n >> i & 1:
            p = i - 2
            ans += dp[i][k-T] + x * math.comb(i,k-T)
            T += 1
            x += pow(2,i,mod)
            ans %= mod
            if T > k: break
    if T == k: ans += n
    print(ans % mod)