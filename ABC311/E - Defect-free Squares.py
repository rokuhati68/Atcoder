h, w, n = map(int, input().split())
ab = set()
for i in range(n):
    a, b = map(int, input().split())
    ab.add((a, b))

dp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
result = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if (i, j) in ab:
            continue
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        result += dp[i][j]

print(result)