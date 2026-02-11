N = int(input())
X,Y = 0,0
ans = 0

for _ in range(N):
    x, y = map(int,input().split())
    dist = pow((X - x) ** 2 + (Y - y) ** 2,0.5)
    ans += dist
    X,Y = x,y

ans += pow((X - 0) ** 2 + (Y - 0) ** 2,0.5)
print(ans)