from atcoder.segtree import SegTree
N, Q = map(int,input().split())
A = list(map(int,input().split()))


def op(l,r):
    lf,lfc,ls,lsc = l
    rf,rfc,rs,rsc = r
    if lf == rf:
        if ls == rs:
            return(lf,lfc + rfc,ls,lsc+rsc)
        elif ls > rs:
            return(lf,lfc + rfc,ls,lsc)
        elif ls < rs:
            return(lf,lfc + rfc,rs,rsc)
    elif lf > rf:
        if rf == ls:
            return(lf,lfc,rf,rfc + lsc)
        elif rf > ls:
            return(lf,lfc,rf,rfc)
        elif rf < ls:
            return(lf,lfc,ls,lsc)
    elif lf < rf:
        if rs == lf:
            return(rf,rfc,rs,rsc + lfc)
        elif rs > lf:
            return(rf,rfc,rs,rsc)
        elif rs < lf:
            return(rf,rfc,lf,lfc)

e = (-1,0,-2,0)
l = []
for a in A:
    l.append((a,1,-1,0))
seg = SegTree(op,e,l)
for _ in range(Q):
    q,l,r = map(int,input().split())
    if q == 1:
        seg.set(l - 1,(r,1,-1,0))
    else:
        print(seg.prod(l-1,r)[3])