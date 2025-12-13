N = int(input())
l = [list(map(int,input().split()))for _ in range(N)]

dp = [False]*(1 << N)
for s in range(1,1<<N):
    for i in range(N):
        if s >> i & 1 != 1:
            continue
        for j in range(N):
            if i == j:
                continue
            if s >> j & 1 != 1:
                continue
            if l[i][0] == l[j][0] or l[i][1] == l[j][1]:
                pre = s
                pre ^= (1<<i)
                pre ^= (1<<j)
                dp[s] |= not dp[pre]

if dp[(1<<N) - 1]:
    print("Takahashi")
else:
    print("Aoki")



