from collections import deque
N , M = map(int,input().split())
S = input().strip()
C = list(map(int,input().split()))

l = [deque() for _ in range(M)]
for i in range(N):
    c = C[i]
    l[c - 1].append(i)

for i in range(M):
    a = l[i].pop()
    l[i].appendleft(a)

for c in C:
    a = l[c - 1].popleft()
    print(S[a],end="")
    