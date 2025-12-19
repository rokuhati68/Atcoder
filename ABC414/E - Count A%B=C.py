N = int(input())
MOD = 998244353

ans = N * (N + 1) //2
ans %= MOD

M = int(pow(N,0.5))
ans += M * M
ans %= MOD

pre = 0
for i in range(1,M + 1):
    pre += N // i
    pre %= MOD

pre *= 2
pre%= MOD
ans += MOD - pre
ans %= MOD

print(ans)