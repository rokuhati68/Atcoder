N = int(input())
K = list(map(int,input().split()))


ans = 10**10

for b in range(2**N):
    left = 0
    right = 0
    for i in range(N):
        if b >> i &1:
            left += K[i]
        else:
            right += K[i]
    
    
    ans = min(ans,max(left,right))

print(ans)