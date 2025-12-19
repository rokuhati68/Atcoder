from itertools import combinations
from collections import defaultdict
N, K = map(int,input().split())

XY = []
for _ in range(N):
    x,y = map(int,input().split())
    XY.append((x,y))
    
if N == 1 or K == 1:
    print("Infinity")
    exit()



dic = defaultdict(int)
l = [i for i in range(N)]
for a,b in combinations(l,2):
    x1,y1 = XY[a]
    x2,y2 = XY[b]
    dx = x1 - x2
    dy = y1 - y2
    cnt = 2
    for c in range(N):
        if a == c or b == c:
            continue
        x3,y3 = XY[c]
        dxx = x1 - x3
        dyy = y1 - y3
        if dx * dyy != dy * dxx:
            continue
        if dx == 0:
            if x3 == x1:
                cnt += 1
        elif dy == 0:
            if y3 == y1:
                cnt += 1
        elif y3 * dx == dy * (x3 - x1) + y1*dx:
            cnt += 1
    if cnt >= K:
        dic[cnt] += 1


ans = 0
for key, value in dic.items():
    div = key * (key -1) // 2
    ans += value // div

print(ans)