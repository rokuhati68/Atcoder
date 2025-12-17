a,b,c = map(int, input().split())
dp = [[[10**18]*101 for _ in range(101)] for _ in range(101)]
for i in range(100,-1,-1):
  for j in range(100,-1,-1):
    for k in range(100,-1,-1):
      if max(i,j,k) == 100:
        dp[i][j][k] = 0
        continue
      bo = i+j+k
      if bo == 0:
        continue
      cur = dp[i+1][j][k]*i+dp[i][j+1][k]*j+dp[i][j][k+1]*k
      dp[i][j][k] = cur/bo + 1

print(dp[a][b][c])