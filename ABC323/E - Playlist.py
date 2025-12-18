n,x=map(int,input().split())
T=list(map(int,input().split()))
dp=[0]*(x+1)
dp[0]=1
mod=998244353
ninv=pow(n,mod-2,mod)
for i in range(x):
    for k in T:
        if i+1-k>=0:
            dp[i+1]=(dp[i+1]+(dp[i+1-k]*ninv))%mod
#print(dp)
ans=0
start = max(0,x-T[0]+1)
for i in range(start, x+1):
    ans=(ans+(dp[i]*ninv))%mod
print(ans)