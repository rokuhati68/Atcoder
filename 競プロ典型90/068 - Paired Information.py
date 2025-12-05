from atcoder.dsu import DSU
from collections import deque
N = int(input())
Q = int(input())
uf = DSU(N)
q = deque()

_sum = [0] * N
for i in range(Q):
    T, X, Y, V = map(int,input().split())
    if T == 0:
        _sum[X - 1] = V
    q.append((T, X - 1, Y - 1, V))

A = [0] * N
for i in range(N - 1):
    A[i + 1] = _sum[i] - A[i]
    
while q:
    T, X, Y, V = q.popleft()
    if T == 0:
        uf.merge(X, Y)
        continue
    if uf.same(X, Y) == False:
        print("Ambiguous")
    else:
        diff = V - A[X]
        if (X + Y) % 2 == 1:
            diff *= -1
        print(A[Y] + diff)
        
    