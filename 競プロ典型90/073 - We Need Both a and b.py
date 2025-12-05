import sys
sys.setrecursionlimit(10**9)
N = int(input())

dp = [[0 ,0, 0] for _ in range(N)]
edge = [[] for _ in range(N)]

C = list(map(str,input().split()))
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

MOD = 10 ** 9 + 7
def dfs(now, pre):
    c = C[now]
    if c == "a":
        dp[now][0] += 1
    else:
        dp[now][1] += 1
    val1 = 1
    val2 = 1
    for to in edge[now]:
        if pre == to:
            continue
        dfs(to, now)
        val1 *= (dp[to][0] + dp[to][1] + 2 * dp[to][2])
        if c == "a":
            val2 *= (dp[to][0] + dp[to][2])
        else:
            val2 *= (dp[to][1] + dp[to][2])
    if c == "a":
        dp[now][0] = val2 % MOD
    else:
        dp[now][1] = val2 % MOD
    dp[now][2] = (val1 - val2) % MOD
    
dfs(0, -1)
print(dp[0][2] % MOD)

    