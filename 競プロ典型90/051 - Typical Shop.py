from bisect import bisect_right
N, K, P  = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
N1 = N // 2
N2 = N - N1
A1 = A[:N1]
A2 = A[N1:]

cnt1 = [[]for _ in range(N1+1)]
for b in range(2**N1):
    cnt = 0
    price = 0
    for i in range(N1):
        if b >> i & 1 == 1:
            cnt += 1
            price += A[i]
    cnt1[cnt].append(price)

cnt2 = [[]for _ in range(N2+1)]
for b in range(2**N2):
    cnt = 0
    price = 0
    for i in range(N2):
        if b >>i & 1 == 1:
            cnt += 1
            price += A2[i]
    cnt2[cnt].append(price)

for i in cnt2:
    i.sort()

ans = 0
for i in range(N1+1):
    if K - i > N2:
        continue
    for j in cnt1[i]:
        diff = P - j
        ans += bisect_right(cnt2[K - i],diff)

print(ans)

