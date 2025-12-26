import math
N = int(input())
A = list(map(int,input().split()))
MOD = 10**9 + 7

ans = 0
lcm = math.lcm(*A) % MOD
for i in range(N):
    div = pow(A[i],MOD- 2,MOD)
    ans += lcm * div % MOD

print(ans%MOD)
        