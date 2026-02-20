from atcoder.segtree import SegTree
import math
T = int(input())
MOD = 998244353
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    seg = SegTree(math.lcm,1,A)
    
    for i in range(N):
        if i == 0:
            ans = seg.prod(1,N) % MOD
        elif i == N - 1:
            ans = seg.prod(0,N - 1) % MOD
        else:
            ans = math.lcm(seg.prod(0,i) , seg.prod(i + 1,N)) % MOD
        print(ans,end = " ")
    print()
            
    