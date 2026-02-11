N, M, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
cnt = 0
for i in B:
    if A[i - 1] < K:
        ans += A[i - 1]
        cnt += 1
print(cnt, ans)