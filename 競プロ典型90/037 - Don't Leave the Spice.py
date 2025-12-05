from atcoder.segtree import SegTree

W, N = map(int,input().split())
INF = 10 ** 10
dp = [[- INF] * (W + 1) for _  in range(N + 1)]
dp[0][0] = 0
Seg = SegTree(max, -INF, dp[0])

for i in range(N):
    L, R, V = map(int,input().split())
    for j in range(W + 1):
        if j - L < 0:
            dp[i + 1][j] = dp[i][j]
            continue
        _max = Seg.prod(max(j - R, 0), max(j - L + 1, 1))
        
        if _max != -INF:
            dp[i + 1][j] = max(dp[i][j], _max + V)
        else:
            dp[i + 1][j] = dp[i][j] 
    Seg = SegTree(max, -INF, dp[i + 1])


ans = Seg.get(W)
if ans == -INF:
    print(-1)
else:
    print(ans)