from atcoder.dsu import DSU
from collections import defaultdict
from sortedcontainers import SortedSet
N = int(input())


print(group)
ans = []    
def dfs(now):
    ans.append(group[now])
    for to in edge[now]:
        dfs(to)

dfs(0)
print(*ans)
        
    
        