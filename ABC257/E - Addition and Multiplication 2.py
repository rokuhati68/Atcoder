import sys
sys.setrecursionlimit(10**9)
N = int(input())
C = list(map(int,input().split()))
dp = [-1] * (N + 1)
dp[0] = 0
for i in range(N):
    if dp[i] == -1:
        continue
    for j in range(9):
        if i + C[j] > N:
            continue
        dp[i + C[j]] = max(dp[i + C[j]],dp[i] + 1)

_max = max(dp)
ans = 0
def check(n,now):
    global ans
    if dp[n] == _max:
       print(now)
       exit()
    for i in range(8,-1,-1):
        c = C[i]
        if n + c > N:
            continue
        if dp[n] + 1 == dp[n + c]:
            check(n + c,now + str(i+1))

check(0,"")
print(ans)

        
        