MOD = 998244353
A, B, C, D = map(int, input().split())
N = A + B + C + D

# factorials
fac = [1] * (N + 1)
for i in range(1, N + 1):
    fac[i] = fac[i - 1] * i % MOD

def nCk(n,k):
    return fac[n] * pow(fac[k],MOD -2,MOD) * pow(fac[n - k],MOD - 2, MOD) % MOD

over = nCk(A + B,A) % MOD
ans = 0
for x in range(C + 1):
    left = nCk(A + B + x, B)          
    right = nCk(D + C - x - 1, D - 1)
    ans = (ans + left * right) % MOD

print(ans)
