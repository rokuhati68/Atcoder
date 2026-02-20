N = int(input())
A = list(map(int,input().split()))
dp = [[0] * N for _ in range(341)]

for i in range(N):
    dp[0][i] = A[i] - 1

for i in range(340):
    for j in range(N):
        dp[i + 1][j] = dp[i][dp[i][j]]

for i in range(N):
    ans = i
    for j in range(340):
        if 10**100 >> j & 1 == 1:
            ans = dp[j][ans]
    print(ans + 1,end = " ")

