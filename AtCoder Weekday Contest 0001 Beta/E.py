from atcoder.segtree import SegTree
N, K = map(int,input().split())
H = list(map(int,input().split()))

seghigh = SegTree(max,-10**10,H)
seglow = SegTree(min,10**10,H)

ans = 0
for i in range(N - K + 1):
    _max = seghigh.prod(i,i + K)
    _min = seglow.prod(i,i+K)
    ans = max(ans,_max - _min)
    
print(ans)