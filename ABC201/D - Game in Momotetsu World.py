H, W = map(int,input().split())
A = [input()for _ in range(H)]
dp = [[0] * W for _ in range(H)]

for i in range(H - 1,-1,-1):
    for j in range(W - 1,-1,-1):
        if i == H - 1 and j == W - 1:
            continue
        ans = -10**10
        pre = 0
        if i < H - 1:
            pre = -dp[i + 1][j]
            if A[i + 1][j] == "+":
                pre += 1
            else:
                pre -= 1
            ans = max(ans,pre)
        if j < W - 1:
            pre = - dp[i][j + 1]
            if A[i][j + 1] == "+":
                pre += 1
            else:
                pre -= 1
            ans = max(ans,pre)
        dp[i][j] = ans
        
if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")
