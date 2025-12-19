import sys
sys.setrecursionlimit(10**8)
from collections import deque
N = int(input())
edge = [[]for _ in range(N)]
for _ in range(N - 1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
    
def dfs(now):
    for to in edge[now]:
        if deep[to] < deep[now]:
            continue
        deep[to] = deep[now] + 1
        dfs(to)
        deepsum[now] += deepsum[to]
        childcnt[now] += childcnt[to]
    deepsum[now] += deep[now]
deep = [10**10] * N
deep[0] = 0
deepsum = [0] * N
childcnt = [1] * N
dfs(0)

up = [0] * N
ans = [-1] * N
q = deque()
q.append(0)
while q:
    now = q.popleft()
    ans[now] = up[now] + deepsum[now] - deep[now] * childcnt[now]
    for to in edge[now]:
        if ans[to] == -1:
            up[to] = ans[now] - deepsum[to] + deep[now] * childcnt[to] + (N - childcnt[to])
            q.append(to)

for i in ans:
    print(i)