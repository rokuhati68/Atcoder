from atcoder.lazysegtree import LazySegTree

W,N = map(int,input().split())
def mapping(lazy_upper, data_lower):
    if lazy_upper == -1:
        return data_lower
    else:
        return lazy_upper
    
def composition(lazy_upper,lazy_lower):
    if lazy_upper == -1:
        return lazy_lower
    return lazy_upper

l =[0]*W
seg = LazySegTree(max,0,mapping,composition,-1,l)

for _ in range(N):
    L, R = map(int,input().split())
    L -= 1
    R -= 1
    height = seg.prod(L, R + 1)
    print(height + 1)
    seg.apply(L, R + 1,height + 1)