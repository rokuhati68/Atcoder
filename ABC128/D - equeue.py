from collections import defaultdict
N, K = map(int,input().split())
V = list(map(int,input().split()))

ans = 0
for a in range(N + 1):
    for b in range(N - a + 1):
        if a==0 and b == 0:
            continue
        if a + b > K:
            continue
        l = V[:a] + V[N - b:]
        l.sort()
        for i in range(min(K - a - b,a + b)):
            if l[0] < 0:
                l.pop(0)
            else:
                break
        ans = max(ans,sum(l))

print(ans)