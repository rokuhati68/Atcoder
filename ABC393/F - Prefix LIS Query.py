from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))

queries = [[] for _ in range(N + 1)]
for qi in range(Q):
    r, x = map(int, input().split())
    queries[r].append((qi, x))

INF = 10**18
tails = [INF] * (N + 1)
tails[0] = -INF  # 長さ0の番兵

ans = [0] * Q

# r = 0 のクエリもありうるなら先に処理
for qi, x in queries[0]:
    ans[qi] = bisect_right(tails, x) - 1

for r in range(1, N + 1):
    a = A[r - 1]
    idx = bisect_left(tails, a)
    tails[idx] = a

    for qi, x in queries[r]:
        ans[qi] = bisect_right(tails, x) - 1

print(*ans, sep="\n")
