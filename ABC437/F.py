from atcoder.segtree import SegTree
N, Q = map(int,input().split())
segmax1= SegTree(max,-10**10,N)
segmax2 = SegTree(max,-10**10,N)
segmin1 = SegTree(min,10**10,N)
segmin2 = SegTree(min,10**10,N)

for i in range(N):
    x,y = map(int,input().split())
    segmax1.set(i,x + y)
    segmax2.set(i,x - y)
    segmin1.set(i,x + y)
    segmin2.set(i,x - y)

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        i,x,y = q[1:]
        i -= 1
        segmax1.set(i,x + y)
        segmax2.set(i,x - y)
        segmin1.set(i,x + y)
        segmin2.set(i,x - y)
    else:
        l,r,x,y = q[1:]
        l -= 1
        max1 = segmax1.prod(l,r)
        max2 = segmax2.prod(l,r)
        min1 = segmin1.prod(l,r)
        min2 = segmin2.prod(l,r)
        ans = max(max1 - (x + y),(x + y) - min1,max2 - (x - y),(x - y) - min2)
        print(ans)
