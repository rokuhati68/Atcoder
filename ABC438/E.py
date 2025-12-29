N, Q = map(int,input().split())
A = list(map(int,input().split()))

water = [[0] * N for _ in range(31)]
go = [[0] * N for _ in range(31)]
for i in range(N):
    water[0][i] = i + 1
    go[0][i] = A[i] - 1

for i in range(30):
    for j in range(N):
        go[i + 1][j] = go[i][go[i][j]]
        water[i + 1][j] = water[i][j] + water[i][go[i][j]]


for _ in range(Q):
    t,b = map(int,input().split())
    b -= 1
    ans = 0
    for i in range(31):
        if t >> i & 1 == 1:
            ans += water[i][b]
            b = go[i][b]
    print(ans)
    