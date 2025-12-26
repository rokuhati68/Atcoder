N, X, Y = map(int,input().split())
dp = [-1]*(840)
for i in range(840):
    dp[i] = i + X
for i in range(N - 1):
    p,t = map(int,input().split())
    for j in range(840):
        now = dp[j]
        start = (((now - 1) // p) + 1) * p
        dp[j] = start + t


Q = int(input())
for _ in range(Q):
    q = int(input())
    idx = q % 840
    print(q + dp[idx] + Y - idx)