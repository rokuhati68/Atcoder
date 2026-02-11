N, M = map(int,input().split())

ans = 0
for _ in range(N):
    a,b = map(int,input().split())
    pre = (M - a - 1)//b
    pre += 1
    ans = max(ans,pre)

print(ans)