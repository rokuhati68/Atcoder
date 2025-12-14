from collections import deque,Counter
N = int(input())
A = list(map(int,input().split()))
MOD = 998244353
dp = [[-1] * N for _ in range(N)]
for i in range(N):
    a = A[i]
    for j in range(i,N):
        b = A[j]
        dp[i][j] = b - a


if N == 1:
    print(1)
    exit()
elif N == 2:
    print(2, 1)
    exit()
ans = [0] * N
ans[0] = N
ans[1] = N * (N - 1) // 2
for i in range(N):
    for to in range(i + 1, N):
        diff = dp[i][to]
        if diff == 0:
            continue
        q = deque()
        q.append((to,2))
        while q:
            now, cnt = q.popleft()
            if now == N:
                continue
            for to in range(now + 1, N):
                if dp[now][to] == diff:
                    ans[cnt] += 1
                    ans[cnt] %= MOD
                    q.append((to,cnt + 1))

nCk = [[0] * 82 for _ in range(82)]
dp[0][0] = 1
for n in range(1,82):
    nCk[n][0] = 1
    for k in range(1,n + 1):
        nCk[n][k] = (nCk[n - 1][k - 1] + nCk[n - 1][k]) % MOD
C = Counter(A)

for key, value in C.items():
    if value >= 3:
        for i in range(3,value + 1): 
            ans[i - 1] += nCk[value + 1][i]
            ans[i - 1] %= MOD
print(*ans)
