from functools import cache
import sys
sys.setrecursionlimit(10**8)
N, K = map(int,input().split())
MOD = 10**9
if N < K:
    print(1)
    exit()
l = [1] * K
_sum = K
for i in range(K,N+1):
    _sum -= l[i - K - 1]
    _sum += l[-1]
    _sum %= MOD
    l.append(_sum)


print(_sum)