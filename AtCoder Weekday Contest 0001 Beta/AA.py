N, K = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
   if A[i] == K:
    print(i + 1)
    exit()

print(-1)