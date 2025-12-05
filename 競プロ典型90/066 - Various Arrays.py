N = int(input())

ans = 0
lr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        L, R = lr[i]
        l, r = lr[j]
        cnt = 0
        for val in range(L, R + 1):
            cnt += max(0, min(r, val - 1) - l + 1)
        ans += cnt / ((R - L + 1) * (r - l + 1))
    
print(ans)
            
            
            
        