H,W,K = map(int,input().split())
sy,sx,gy,gx = map(int,input().split())
MOD = 998244353
dp = [0,0,0,0]
if sy == gy and sx == gx:
    dp[3] = 1
elif sx == gx:
    dp[2] = 1
elif sy == gy:
    dp[1] = 1
else:
    dp[0] = 1

for _ in range(K):
    nxt = [0,0,0,0]
    nxt[0] += dp[0] * (H + W - 4) + dp[1] * (H - 1) + dp[2] * (W - 1)
    nxt[0] %= MOD
    nxt[1] += dp[0] + dp[1]*(W - 2) + dp[3] * (W - 1)
    nxt[1] %= MOD
    nxt[2] += dp[0] + dp[2] * (H - 2) + dp[3] * (H - 1)
    nxt[2] %= MOD
    nxt[3] += dp[1] + dp[2]
    nxt[3] %= MOD
    dp = nxt

print(dp[3])    
        