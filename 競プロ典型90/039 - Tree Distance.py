import sys
sys.setrecursionlimit(10**8)
N = int(input())

edge = [[]for _ in range(N)]
for _ in range(N - 1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

dp = [1] * N

def dfs(now,pre):
    for to in edge[now]:
        if to == pre:
            continue
        dp[now] += dfs(to,now)
    return dp[now]

dfs(0,-1)
ans = 0
for i in dp:
    ans += i * (N - i)

print(ans)