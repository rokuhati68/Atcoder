from heapq import heappop, heappush

INF = 10**30

N, M = map(int, input().split())
edge = [[] for _ in range(N)]

U = [0] * (M + 1)
V = [0] * (M + 1)
W = [0] * (M + 1)

for idx in range(1, M + 1):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    U[idx] = u
    V[idx] = v
    W[idx] = c
    edge[u].append((v, c))
    edge[v].append((u, c))

# ---- all-pairs shortest paths via N times Dijkstra (N <= 400) ----
dist = [[INF] * N for _ in range(N)]
for s in range(N):
    dist[s][s] = 0
    pq = [(0, s)]
    while pq:
        d, v = heappop(pq)
        if d != dist[s][v]:
            continue
        for to, w in edge[v]:
            nd = d + w
            if nd < dist[s][to]:
                dist[s][to] = nd
                heappush(pq, (nd, to))

# ---- queries ----
Q = int(input())
S = 0
G = N - 1

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))

    # クエリで使う頂点集合：S, G, 各指定辺の両端
    verts = [S, G]
    req = []
    for e_id in B:
        a = U[e_id]
        b = V[e_id]
        w = W[e_id]
        req.append((a, b, w))
        verts.append(a)
        verts.append(b)

    # unique
    uniq = []
    seen = set()
    for x in verts:
        if x not in seen:
            seen.add(x)
            uniq.append(x)

    idx_map = {v: i for i, v in enumerate(uniq)}
    L = len(uniq)  # <= 12

    # ローカル距離行列
    D = [[0] * L for _ in range(L)]
    for i in range(L):
        di = dist[uniq[i]]
        row = D[i]
        for j in range(L):
            row[j] = di[uniq[j]]

    s_id = idx_map[S]
    g_id = idx_map[G]

    # DP[mask][pos]
    full = (1 << K) - 1
    dp = [[INF] * L for _ in range(1 << K)]
    dp[0][s_id] = 0

    for mask in range(1 << K):
        cur = dp[mask]
        for pos in range(L):
            base = cur[pos]
            if base >= INF:
                continue
            # 次に通る指定辺を選ぶ
            for j in range(K):
                if mask >> j & 1:
                    continue
                a, b, w = req[j]
                ai = idx_map[a]
                bi = idx_map[b]
                nmask = mask | (1 << j)

                # pos -> a ->(edge)-> b
                cost1 = base + D[pos][ai] + w
                if cost1 < dp[nmask][bi]:
                    dp[nmask][bi] = cost1

                # pos -> b ->(edge)-> a
                cost2 = base + D[pos][bi] + w
                if cost2 < dp[nmask][ai]:
                    dp[nmask][ai] = cost2

    ans = min(dp[full][pos] + D[pos][g_id] for pos in range(L))
    print(ans)
