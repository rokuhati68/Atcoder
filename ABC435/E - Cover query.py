from atcoder.lazysegtree import LazySegTree
# 区間更新・区間和取得^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INF = 1 << 63
def op(a,b):
    return a + b

e = 0
def mapping(lazy_upper,lower_data):
    if lazy_upper == _id:
        return lower_data
    else:
        return lazy_upper

def composition(lazy_upper,lazy_lower):
    if lazy_upper ==_id:
        return lazy_lower
    else:
        return lazy_upper

_id = INF
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


N, Q = map(int,input().split())
lr = []
v = set()
for _ in range(q):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    lr.append((l,r))
    v.add(l)
    v.add(r + 1)
v.add(0)
v.add(N)
v = sorted(v)
to_idx = {j: i for i, j in enumerate(v)}

l = [v[i + 1] - v[i] for i in range(len(v) - 1)]

st = LazySegTree(op, e, mapping, composition, _id, l)
for l, r in lr:
    st.apply(to_idx[l], to_idx[r + 1], 0)
    print(st.all_prod())
    