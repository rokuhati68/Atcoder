from itertools import combinations
N = int(input())
l = [list(map(int,input().split()))for _ in range(N)]

def triangle(x1,y1,x2,y2,x3,y3):
    area = abs(x1*(y2 - y3) + x2 * (y3 - y1) + x3*(y1 - y2))
    if area == 0:
        return 0
    elif area % 2 == 0:
        return 1
    else:
        return 0

ll = [i for i in range(N)]
ans = 0
for i,j,r in combinations(ll,3):
    a = l[i]
    b = l[j]
    c = l[r]
    ans += triangle(a[0],a[1],b[0],b[1],c[0],c[1])

print(ans)