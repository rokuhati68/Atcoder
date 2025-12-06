S = input()
_len= len(S)
dp = [[0] * 13 for _ in range(_len + 1)]
MOD = 10**9 + 7
dp[0][0] = 1

for i in range(_len):
    if S[i] != "?":
        num = int(S[i])
        for j in range(13):
            dp[i + 1][(10*j + num)%13] += dp[i][j]
            dp[i + 1][(10*j + num)%13] %= MOD
    else:
        for num in range(10):
            for j in range(13):
                dp[i + 1][(10*j + num)%13] += dp[i][j]
                dp[i + 1][(10*j + num)%13] %= MOD

print(dp[-1][5])