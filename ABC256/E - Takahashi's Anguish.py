from atcoder.scc import SCCGraph
N = int(input())
X = list(map(int,input().split()))
C = list(map(int,input().split()))
sg = SCCGraph(N)
for i in range(N):
    sg.add_edge(i,X[i] - 1)
ans = 0
for v in sg.scc():
    if len(v) == 1:
        continue
    pre = 10**10
    for i in v:
        pre = min(pre,C[i])
    ans += pre

print(ans)
