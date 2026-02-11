N, M = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))
C.sort(reverse = True)
R.sort()

ans = 0
for i in R:
    if len(C) == 0:
        break
    if i >= C[-1]:
        ans += 1
        C.pop()
        

print(ans)