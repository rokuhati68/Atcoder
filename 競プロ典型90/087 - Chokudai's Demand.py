def warshall_floyd(X):
  dist = [[10**18]*N for _ in range(N)]
  
  for i in range(N):
    for j in range(N):
      dist[i][j] = A[i][j] if A[i][j] != -1 else X
  
  for k in range(N):
    for i in range(N):
      for j in range(N):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  
  cnt = 0
  for i in range(N):
    for j in range(i+1, N):
      if dist[i][j] <= P:
        cnt += 1
  
  return cnt

N, P, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]

ok1 = 10**18
ng1 = 0

while ok1 - ng1 > 1:
  mid = (ok1 + ng1)//2
  if warshall_floyd(mid) <= K:
    ok1 = mid
  else:
    ng1 = mid

ok2 = 10**18
ng2 = 0

while ok2 - ng2 > 1:
  mid = (ok2 + ng2)//2
  if warshall_floyd(mid) <= K-1:
    ok2 = mid
  else:
    ng2 = mid

print("Infinity" if ok1 != 10**18 and ok2 == 10**18 else ok2-ok1)