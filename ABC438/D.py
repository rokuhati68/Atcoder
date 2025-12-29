N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

diffB = []
diffC = []
for i in range(N):
    diffB.append(B[i] - A[i])
    diffC.append(C[i] - B[i])
_sumB = []
_sumC = []
pre = 0
prec = 0
for i in range(N-1,0,-1):
    pre +=diffB[i]
    _sumB.append(pre)
    prec += diffC[i]
    _sumC.append(prec)
_sumB = _sumB[::-1]
_sumC = _sumC[::-1]

_max = _sumB[0]
for i in range(1,N - 1):
    _max = max(_max,_sumB[i])
    _sumB[i] = _max

ans = -10**30
for i in range(1,N - 1):
    ans = max(ans,_sumC[i] + _sumB[i - 1])

print(sum(A) + ans)
