N = int(input())
A = list(map(int,input().split()))
lcm = [0]
for i in range(N):
    a = A[i]
    lcm.append(lcm[i] + a)

ans = 0
for l in range(N):
    for r in range(l+1,N + 1):
        isOK = True
        _sum = lcm[r] - lcm[l]
        for i in range(l,r):
            if _sum % A[i] == 0:
                isOK = False
                break
        if isOK:
            ans += 1
    
print(ans)