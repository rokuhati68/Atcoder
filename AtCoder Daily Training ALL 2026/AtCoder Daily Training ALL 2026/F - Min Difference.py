from bisect import bisect_left
N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.append(-10**10)
A.append(10**10)
A.sort()
B.sort()
ans = 10**10

for i in B:
    idx = bisect_left(A,i)
    ans = min(ans,i - A[idx - 1], A[idx] - i)
    
    
print(ans)
    