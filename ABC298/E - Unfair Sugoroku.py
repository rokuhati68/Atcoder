N, A, B, P , Q = map(int,input().split())
MOD = 998244353

divP = pow(P,MOD - 2,MOD)
divQ = pow(Q,MOD - 2,MOD)
dpT = [[0] * (N + 1)for _ in range(N + 1)]
dpT[0][A] = 1
dpA = [[0] * (N + 1)for _ in range(N + 1)]
dpA[0][B] = 1
for i in range(N):
    for j in range(N):
        dpT[i + 1][j] = sum(dpT[i][max(0,j - P):j]) * divP % MOD
        dpA[i + 1][j] = sum(dpA[i][max(0,j - Q):j]) * divQ % MOD
    for j in range(1,P + 1):
        if N - j < 0:
            continue
        dpT[i + 1][N] += dpT[i][N - j] * divP * (P - j + 1) % MOD
        dpT[i + 1][N] %= MOD
    for j in range(1,Q + 1):
        if N - j < 0:
            continue
        dpA[i + 1][N] += dpA[i][N - j] * divQ * (Q - j + 1) % MOD
        dpA[i + 1][N] %= MOD
        

ans = 0
A = [0]
pre = 0
for i in range(N):
    pre += dpA[i + 1][N]
    pre %= MOD
    A.append(pre)

for i in range(N):
    preans = dpT[i + 1][N] * (1 - A[i]) % MOD
    ans += preans
    ans %= MOD

print(ans)