from atcoder.scc import SCCGraph

N, M = map(int,input().split())
graph = SCCGraph(N)
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    graph.add_edge(a,b)

ans = 0
for i in graph.scc():
    _len = len(i)
    ans += _len * (_len - 1) // 2

print(ans)