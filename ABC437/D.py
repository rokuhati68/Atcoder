from bisect import bisect_left
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
MOD = 998244353
lcmA = [0]
pre = 0
for a in A:
    pre += a
    pre %= MOD
    lcmA.append(pre)

ans = 0
for b in B:
    idx = bisect_left(A,b)
    ans += pre - 2*lcmA[idx] + (2*idx - N) * b
    ans += MOD
    ans %= MOD

print(ans)