W,B = map(int,input().split())

W *= 1000
ans = 0

while ans * B <= W:
    ans += 1

print(ans)