from atcoder.lazysegtree import LazySegTree

N,Q = map(int,input().split())
A = list(map(int,input().split()))
INF = 1 << 63
ID = INF
def op(ele1, ele2):
    return ele1 + ele2


def mapping(func, ele):
    if func == ID:
        return ele
    else:
        return func


def composition(func_upper, func_lower):
    if func_upper == ID:
        return func_lower
    else:
        return func_upper
e = 0
id_ = ID
seg = LazySegTree(op, e, mapping, composition, id_, A)
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1]) - 1
        num1 = seg.get(x)
        num2 = seg.get(x + 1)
        seg.set(x,num2)
        seg.set(x + 1,num1)
    else:
        l = int(query[1]) - 1
        r = int(query[2])
        ans = seg.prod(l,r)
        print(ans)