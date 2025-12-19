H , W = map(int,input().split())
S = [input()for _ in range(H)]
lcmH = [[0] * W for _ in range(H + 1)]
lcmW = [[0] * H for _ in range(W + 1)]
lcmHW = [[0] * (int(pow(H * W,0.5)))for _ in range(H + W - 1)]

isOK = True
for i in range(1,W):
    if S[0][i] == ".":
        lcmW[i][0] = 1
        if isOK:
            lcmH[0][i] = 2 ** (i - 1)
            lcmHW[- i + W - 1][0] = 2**(i - 1)
    else:
        isOK = False
isOK = True
for i in range(1,H):
    if S[i][0] == ".":
        lcmH[i][0] = 1
        if isOK:
            lcmW[0][i] = 2**(i-1)
            lcmHW[i + W - 1][0] = 2**(i-1)
    else:
        isOK = False

lcmHW[W - 1][0] = 1


MOD = 10**9 + 7
for i in range(1,H):
    for j in range(1,W):
        if S[i][j] == "#":
            continue
        else:
            prelcmH = lcmH[i - 1][j]
            prelcmW = lcmW[j - 1][i]
            prelcmHW = lcmHW[i - j + W - 1][min(i,j) - 1]
            _sum = (prelcmH + prelcmW + prelcmHW) % MOD
            lcmH[i][j] = ((prelcmH + _sum) % MOD)
            lcmW[j][i] = ((prelcmW + _sum) % MOD)
            lcmHW[i - j + W - 1][min(i,j)] = ((prelcmHW + _sum) % MOD)

print(_sum)