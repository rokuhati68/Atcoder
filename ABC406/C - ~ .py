from itertools import groupby

N = int(input())
P = list(map(int,input().split()))
S = []
for i in range(N - 1):
    if P[i] > P[i + 1]:
        S.append(">")
    else:
        S.append("<")

G = []
for key, group in groupby(S):
    G.append((key,len(list(group))))

ans = 0
for i in range(1,len(G) - 1):
    pre = G[i - 1]
    now = G[i]
    nxt = G[i + 1]
    if pre[0] == "<" and now[0] == ">" and nxt[0] == "<":
        ans += pre[1] * nxt[1]
        
print(ans)