from collections import deque
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

C = list(map(int,input().split()))
all_sum = sum(C)
child_sum = C[:]
dist = [-1] * N
dist[0] = 0
def dfs(now,pre):
    for to in edge[now]:
        if to == pre:
            continue
        dist[to] = dist[now] + 1
        dfs(to,now)
        child_sum[now] += child_sum[to]

dfs(0,-1)
ans = 0
for i in range(N):
    ans += C[i] * dist[i]


q = deque()
q.append((0,-1,ans))
while q:
    now,pre,_sum = q.popleft()
    for to in edge[now]:
        if to == pre:
            continue
        nxt_sum = _sum + all_sum - 2*child_sum[to]
        ans = min(ans,nxt_sum)
        q.append((to,now,nxt_sum))

print(ans)