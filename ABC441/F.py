import sys
input = sys.stdin.readline

INF = 10**30

N, M = map(int, input().split())
P = [0]*N
V = [0]*N
for i in range(N):
    P[i], V[i] = map(int, input().split())

# dpR[i] = items i..N-1 だけで価格 w の最大価値 (iは0-index)
# dpR[N] は空集合（0以外は到達不可）
dpR = [None] * (N + 1)
dp = [-INF] * (M + 1)
dp[0] = 0
dpR[N] = dp[:]  # copy

for i in range(N - 1, -1, -1):
    p, v = P[i], V[i]
    # 0/1 knap update (descending)
    ndp = dp[:]  # copy current dp as base
    for w in range(M - p, -1, -1):
        if dp[w] != -INF:
            val = dp[w] + v
            if val > ndp[w + p]:
                ndp[w + p] = val
    dp = ndp
    dpR[i] = dp[:]  # store row

OPT = max(dpR[0])  # 全体最適

# 前から dpL を作りつつ判定
dpL = [-INF] * (M + 1)
dpL[0] = 0

ans = []

for i in range(N):
    dpR_after = dpR[i + 1]

    # bestS[c] = max_{w<=c} dpR_after[w]
    bestS = dpR_after[:]  # copy
    for c in range(1, M + 1):
        if bestS[c - 1] > bestS[c]:
            bestS[c] = bestS[c - 1]

    # best without i
    best_without = -INF
    for w in range(M + 1):
        if dpL[w] == -INF:
            continue
        cand = dpL[w] + bestS[M - w]
        if cand > best_without:
            best_without = cand

    # best with i
    p, v = P[i], V[i]
    best_with = -INF
    cap = M - p
    if cap >= 0:
        for w in range(cap + 1):
            if dpL[w] == -INF:
                continue
            cand = dpL[w] + v + bestS[cap - w]
            if cand > best_with:
                best_with = cand

    if best_with < OPT:
        ans.append("C")
    else:
        if best_without < OPT:
            ans.append("A")
        else:
            ans.append("B")

    # dpL を次に進める（i を使えるように更新）
    # 0/1 knap update (descending)
    for w in range(M - p, -1, -1):
        if dpL[w] != -INF:
            val = dpL[w] + v
            if val > dpL[w + p]:
                dpL[w + p] = val

print("\n".join(ans))
