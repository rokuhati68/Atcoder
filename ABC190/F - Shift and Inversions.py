from sortedcontainers import SortedList
from atcoder.fenwicktree import FenwickTree
N = int(input())
A = list(map(int,input().split()))
fw = FenwickTree(N)
_sum = 0
for i in range(N):
    a = A[i]
    _sum +=fw.sum(a + 1,N)
    fw.add(a,1)
print(_sum)
sl = SortedList(A)
for i in range(N - 1):
    a = A[i]
    idx = sl.bisect_left(a)
    _sum -= idx
    idx = sl.bisect_right(a)
    _sum += (N - idx)
    print(_sum)
    

