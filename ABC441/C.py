N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


B = A[:K]

if sum(B) < X:
    print(-1)
    exit()

s = 0
for t in range(1, K + 1):
    s += B[-t]
    if s >= X:
        print((N - K) + t)
        break
