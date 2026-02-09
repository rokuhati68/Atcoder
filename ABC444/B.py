N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    pre = 0
    while i > 0:
        pre += i % 10
        i //= 10
    if pre == K:
        ans += 1

print(ans)