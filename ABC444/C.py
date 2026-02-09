from bisect import bisect_left
N = int(input())
A = list(map(int,input().split()))

A.sort()
AA = A[::-1]
ans = []
sumL = A[0] + A[-1]
if N % 2 == 0:
    isOK = True
    for i in range(N // 2):
        if(A[i] + AA[i] != sumL):
            isOK = False
            break
    if isOK:
        ans.append(sumL)


_maxA = A[-1]
idx = bisect_left(A,_maxA)
AA = A[:idx]
AAA = AA[::-1]
if len(AA) % 2 ==0:
    isOK = True
    for i in range(len(AA)//2):
        if(AA[i] + AAA[i]) != _maxA:
            isOK = False
            break
    if isOK:
        ans.append(_maxA)

ans.sort()
print(*ans)