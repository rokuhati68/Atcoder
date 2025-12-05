from bisect import bisect_left
N = int(input())
A = list(map(int,input().split()))
dp1 = [0]
dp2 = [0]

cnt1 = 1
cnt2 = 1
P = []
Q = []
for i in range(N):
    a = A[i]
    b = A[N - i - 1]
    idx1 = bisect_left(dp1, a)
    idx2 = bisect_left(dp2, b)
    P.append(idx1)
    Q.append(idx2)
    if idx1 == cnt1:
        dp1.append(a)
        cnt1 += 1
    else:
        dp1[idx1] = min(dp1[idx1], a)
    if idx2 == cnt2:
        dp2.append(b)
        cnt2 += 1
    else:
        dp2[idx2] = min(dp2[idx2], b)

ans= 0
for i in range(N):
    ans = max(ans, P[i] + Q[N - i - 1] - 1)

print(ans)

