import sys
sys.setrecursionlimit(10**8)
N = int(input())
x = list(map(int,input().split()))

edge = [[]for _ in range(N)]
for _ in range(N - 1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append((v,w))
    edge[v].append((u,w))

ans = 0
def dfs(now,pre):
    global ans
    for to,w in edge[now]:
        if to == pre:
            continue
        dfs(to,now)
        ans += abs(x[to]) * w
        x[now] += x[to]

dfs(0,-1)
print(ans)
