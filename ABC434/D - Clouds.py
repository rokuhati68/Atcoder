N = int(input())
HW = [[0] * 2001 for _ in range(2001)]
num = [[0] * 2001 for _ in range(2001)]

for i in range(N):
    u,d,l,r = map(int,input().split())
    u -= 1
    d -= 1
    l -= 1
    r -= 1
    i += 1
    HW[u][l] += 1
    HW[u][r + 1] -= 1
    HW[d + 1][l] -= 1
    HW[d + 1][r + 1] += 1
    num[u][l] += i
    num[u][r + 1] -= i
    num[d + 1][l] -= i
    num[d + 1][r + 1] += i
    

for i in range(2001):
    for j in range(2000):
        HW[i][j + 1] += HW[i][j]
        num[i][j + 1] += num[i][j]

for i in range(2001):
    for j in range(2000):
        HW[j + 1][i] += HW[j][i]
        num[j + 1][i] += num[j][i]


cnt = 0
l = [0] * N
for i in range(2000):
    for j in range(2000):
        if HW[i][j] == 0:
            cnt += 1
        elif HW[i][j] == 1:
            n = num[i][j] - 1
            l[n] += 1

for i in l:
    print(cnt + i)