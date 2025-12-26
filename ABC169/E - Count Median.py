N = int(input())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()

if N % 2 == 0:
    amed = (A[(N // 2) - 1] + A[(N // 2)])
    bmed = (B[(N // 2) - 1] + B[N // 2]) 
else:
    amed = A[N // 2]
    bmed = B[N // 2]

print(bmed - amed+ 1)