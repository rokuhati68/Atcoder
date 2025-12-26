N = int(input())
t,a = map(int,input().split())
ans = t + a
left = t
right = a
for _ in range(N - 1):
    t,a = map(int,input().split())
    x1 = (left - 1)//t
    x2 = (right - 1) // a
    x = max(x1,x2) + 1
    left = t*x
    right = a*x
print(left+right)