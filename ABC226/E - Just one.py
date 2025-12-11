from atcoder.dsu import DSU
import sys
sys.setrecursionlimit(10**8)
N, M = map(int,input().split())
edge = [[]for _ in range(N)]
uf = DSU(N)
for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
    uf.merge(u,v)

def dfs(now,pre):
    global cycle
    seen[now] = True
    for to in edge[now]:
        if  to == pre:
            continue
        if finished[to]:
            continue
        if seen[to] and finished[to]==False:
            cycle += 1    
            continue
        dfs(to,now)
    finished[now] = True
    
ans = 0
seen = [False] * N
finished = [False] * N
for g in uf.groups():
    if len(g) <= 2:
        print(0)
        exit()    
    cycle = 0
    dfs(g[0],-1)
    if cycle == 1:
        ans += 1
    else:
        print(0)
        exit()

MOD = 998244353
print(pow(2,ans,MOD))