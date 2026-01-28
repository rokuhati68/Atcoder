N, K, X = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse = True)

_max1 = A[0]
_max2 = A[1]
diff = _max1 - _max2
ans = _max1 * K
for i in range(X):
    print(ans - diff * i)
    