from bisect import bisect_right
N = 10**6
prime = [0] * (N + 1)
for i in range(2,N + 1):
    if prime[i] == 0:
        for to in range(i + i,N+1, i):
            prime[to] += 1

squarNum = []
for i in range(N + 1):
    if prime[i] == 2:
        squarNum.append(i * i)

Q = int(input())
for _ in range(Q):
    q = int(input())
    idx = bisect_right(squarNum,q)
    print(squarNum[idx-1])