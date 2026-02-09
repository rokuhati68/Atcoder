S = input().strip()
dp = [[0] * 26 for _ in range(len(S) + 1)]

for i in range(len(S)):
    for j in range(26):
        dp[i + 1][j] += dp[i][j]
    dp[i + 1][ord(S[i]) - ord("A")] += 1

ans = 0
for i in range(1,len(S) - 1):
    for j in range(26):
        ans += (dp[-1][j] - dp[i + 1][j]) * dp[i][j]

print(ans)