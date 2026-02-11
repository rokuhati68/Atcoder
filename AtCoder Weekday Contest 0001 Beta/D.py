from collections import deque
N, M , K = map(int,input().split())
l = []

dp = [[-1]*(M + 1) for _ in range(N)]
for i in range(N):
    a,b = map(int,input().split())
    dp[i][b] = a
    l.append((a,b))
for i in range(N):
    for j in range(M):
        if dp[i][j] == -1:
            continue
        for k in range(1,K + 1):
            to = i + k
            if to >= N:
                continue
            a,b = l[to]
            if j + b > M:
                continue
            dp[to][j + b] = max(dp[to][j + b] ,dp[i][j] + a)


ans = 0
for i in dp:
    ans = max(ans,max(i))
    
print(ans)