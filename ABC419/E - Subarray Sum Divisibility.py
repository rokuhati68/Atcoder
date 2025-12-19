N, M, L = map(int, input().split())
A = list(map(int, input().split()))
INF = 1<<60

dp = [[0]*M for _ in range(L)]
for i in range(L):
  for j in range(i, N, L):
    for k in range(M):
      dp[i][k] += (k - A[j]) % M

dp1 = dp[0][:]
for k in range(1, L):
  ndp1 = [INF]*M
  for i in range(M):
    for j in range(M):
      ndp1[(i+j)%M] = min(ndp1[(i+j)%M],  dp1[i]+dp[k][j])
  dp1 = ndp1

print(dp1[0])