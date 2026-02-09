
import sys
sys.setrecursionlimit(10**8)



    

def check():
    def dfs(now):
        if now == Y:
            path.append(Y + 1)
            return True
        visited[now] = True
        path.append(now+1)
        for to in l[now]:
            if visited[to]:
                continue
            if dfs(to):
                return True
        path.pop()
        return False
    
    N,M,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    l = [[]for _ in range(N)]
    for _ in range(M):
        u, v = map(int,input().split())
        u-= 1
        v -= 1
        l[u].append(v)
        l[v].append(u)
    for i in range(N):
        l[i].sort()
        
    visited = [False] * N
    path = []
    dfs(X)
    print(*path)
            
    








T = int(input())
for _ in range(T):
    check()
    