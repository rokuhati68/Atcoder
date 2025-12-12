from atcoder.dsu import DSU

N, M = map(int,input().split())
edge =[]
for _ in range(M):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    edge.append((u,v,w))

ans = 2**30 - 1
for k in range(29,-1,-1):
    ans ^= (1<<k)
    uf = DSU(N)
    for u,v,w in edge:
        if (ans | w) == ans:
            uf.merge(u,v)
    if not uf.same(0,N - 1):
        ans |= (1<<k)

print(ans)


