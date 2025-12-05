N, K = map(int,input().split())

css = [[0] * 5001 for _ in range(5001)]
for _ in range(N):
    a, b = map(int,input().split())
    css[a][b] += 1

for i in range(5000):
    for j in range(5000):
        css[i][j + 1] += css[i][j]
for j in range(5000):
    for i in range(5000):
        css[i + 1][j] += css[i][j]

ans = 0
for i in range(1,5000):
    for j in range(1,5000):
        ans = max(ans, css[min(i + K, 5000)][min(j + K, 5000)] - css[i - 1][min(j + K, 5000)] - css[min(i + K, 5000)][j - 1] + css[i - 1][j - 1])

print(ans)