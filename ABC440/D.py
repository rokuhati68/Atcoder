from bisect import bisect_left,bisect_right
from sortedcontainers import SortedList
N, Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
leftList = SortedList()
cnt = [0]
pre = 0
precnt = 0
if A[0] == 1:
    leftList.add((0,0))
for i in range(N):
    nxt = A[i]
    if pre + 1 == nxt:
        pre = nxt
        continue
    leftList.add((pre + 1,nxt - 1))
    precnt += nxt - pre - 1
    cnt.append(precnt)
    pre = nxt

leftList.add((pre+1,10**9 + 1))
precnt += 10**9 - pre - 1
cnt.append(precnt)
print(leftList)
print(cnt)
A = set(A)
for _ in range(Q):
    x,y = map(int,input().split())
    idx = leftList.bisect_right((x,0))
    if x in A:
        preCnt = cnt[idx - 1]
    else:
        preCnt = cnt[idx - 2] + (x - leftList[idx - 1][0])
    target = preCnt + y
    targetidx = bisect_right(cnt,target)
    diff = target - cnt[targetidx - 1]
    print(leftList[targetidx][0] + diff)
    
    