N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    to = min(i + A[i],N)-1
    ans = max(ans,to)
    if ans == i:
        print(ans + 1)
        exit()
    
print(N)