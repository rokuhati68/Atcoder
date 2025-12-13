from atcoder.segtree import SegTree
N, Q = map(int,input().split())
S = input()

def op(a,b):
    return a + b

sg = SegTree(op,0,N + 1)
for i in range(N - 1):
    if S[i] != S[i + 1]:
        sg.set(i + 1,1)


for _ in range(Q):
    q,l,r = map(int,input().split())
    if q == 1:
        pre = sg.get(l - 1)
        sg.set(l - 1, 1 - pre)
        pre = sg.get(r)
        sg.set(r, 1 - pre)
        sg.set(0,0)
        sg.set(N,0)
    else:
        _sum = sg.prod(l,r)
        if _sum == (r - l):
            print("Yes")
        else:
            print("No")
