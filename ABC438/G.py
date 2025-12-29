import math
N ,M , K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
MOD = 998244353

lcm = math.lcm(N,M)
_sum = [0]
pre =0
for i in range(lcm):
    pre += min(A[i % N],B[i%M])
    pre %= MOD
    _sum.append(pre)

ans = 0
div,mod = divmod(K,lcm)
ans += pre * div
ans %= MOD
ans += _sum[mod]
ans %=MOD
print(ans)