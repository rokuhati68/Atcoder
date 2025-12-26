from functools import cache

N = int(input())
MOD = 998244353
div = pow(5,MOD - 2,MOD)

@cache 
def dfs(now):
    if now == 1:
        return 1
    ans = 0
    for i in range(2,7):
        if now % i == 0:
            ans += dfs(now // i)
            ans %= MOD
    
    ans *= div % MOD
    return ans % MOD

print(dfs(N)%MOD)
    