from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    edge = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)

    INF = 10**18
    dist = [[INF]*N for _ in range(N)]

    # (a, b) = (N-1, 0) から逆向き BFS
    q = deque()
    dist[0][N - 1] = 0
    q.append((0, N - 1))

    while q:
        a, b = q.popleft()
        d = dist[a][b]

        for na in edge[a]:
            for nb in edge[b]:
                if C[na] == C[nb]:
                    continue
                if dist[na][nb] > d + 1:
                    dist[na][nb] = d + 1
                    q.append((na, nb))

    ans = dist[N - 1][0]
    print(-1 if ans == INF else ans)
