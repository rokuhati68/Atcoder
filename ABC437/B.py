H, W, N = map(int,input().split())
A = [list(map(int,input().split()))for _ in range(H)]
ans = [0] * N
for _ in range(N):
    b = int(input())
    for i in range(H):
        if b in A[i]:
            ans[i] += 1

print(max(ans))