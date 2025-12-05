N, S = map(int,input().split())
dp = [[False]*(S + 1)for _ in range(N + 1)]
l = []
for _ in range(N):
    a,b = map(int,input().split())
    l.append((a,b))

dp[0][0] = True
for i in range(N):
    a,b = l[i]
    for j in range(S):
        if dp[i][j]:
            if a + j <= S:
                dp[i + 1][j + a] = True
            if b + j <= S:
                dp[i + 1][j + b] = True

if dp[-1][S] == False:
    print("Impossible")
    exit()

ans = []
price = S
for i in range(N, 0, -1):
    a,b = l[i - 1]
    if price - a >= 0 and dp[i - 1][price - a]:
        ans.append("A")
        price -= a
    else:
        ans.append("B")
        price -= b

ans.reverse()
print("".join(ans))