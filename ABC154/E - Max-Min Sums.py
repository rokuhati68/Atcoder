N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
MOD = 10**9 + 7

# K==1 のときは max=min なので差は0
if K == 1:
    print(0)
    exit()

# factorial / inv_factorial
fact = [1] * (N + 1)
invfact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD

invfact[N] = pow(fact[N], MOD - 2, MOD)
for i in range(N, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

def comb(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

# 最大として使われる回数
mx = 0
for i in range(K - 1, N):
    mx = (mx + A[i] * comb(i, K - 1)) % MOD

# 最小として使われる回数（小さい方から見て i を最小にするには右側から K-1 個選ぶ）
mn = 0
for i in range(0, N - K + 1):
    mn = (mn + A[i] * comb(N - i - 1, K - 1)) % MOD

print((mx - mn) % MOD)
