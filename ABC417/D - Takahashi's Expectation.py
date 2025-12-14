from bisect import *
n = int(input())
p = []
a = []
b = []
m = 1000
for i in range(n):
    x, y, z = map(int, input().split())
    p.append(x)
    a.append(y)
    b.append(z)

dp = [[0]*(m+1) for _ in range(n+1)]
for j in range(m+1):
    dp[n][j] = j

for i in range(n)[::-1]:
    for j in range(m+1):
        if j <= p[i]:
            dp[i][j] = dp[i+1][j+a[i]]
        else:
            dp[i][j] = dp[i+1][j-min(j, b[i])]

csum = [0]
for x in b:
    csum.append(csum[-1]+x)


def f(x):
    if x <= m:
        return dp[0][x]

    if x-m >= csum[-1]:
        return x-csum[-1]

    y = x-m
    i = bisect_left(csum, y)
    return dp[i][x-csum[i]]


for _ in range(int(input())):
    x = int(input())
    print(f(x))
