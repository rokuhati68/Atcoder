N, M = map(int,input().split())
A = list(map(int,input().split()))

_sum = sum(A)
diff = _sum - M
if diff in A:
    print("Yes")
else:
    print("No")