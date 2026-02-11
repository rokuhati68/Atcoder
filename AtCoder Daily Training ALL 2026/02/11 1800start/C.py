N = int(input())
A = list(map(int,input().split()))
lcm = [0]
for a in A:
    lcm.append(lcm[-1] + a)
    
ans = 0
for l in range(N):
    for r in range(l + 1,N + 1):
        _sum = lcm[r] - lcm[l]
        isOK = True
        for i in range(l,r):
            if _sum % A[i] == 0:
                isOK = False
                break
        if isOK:
            ans += 1

print(ans)