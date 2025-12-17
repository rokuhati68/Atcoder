from atcoder.segtree import SegTree
N = int(input())
H = [10**10] + list(map(int,input().split())) + [10**10]
H2 = set(H)
H2 = sorted(list(H2))
dic = {}

for i in range(len(H2)):
    h = H2[i]
    dic[h] = i

_len = len(H2)
Seg = SegTree(max,-10**10,_len)
Seg.set(_len-1,0)
ans = [1]
pre = 1

for i in range(1,N + 1):
    h = H[i]
    Seg.set(dic[h],i)
    if H[i - 1] > H[i]:
        pre += H[i]
        ans.append(pre)
    else:
        prehindex = Seg.prod(dic[h] + 1,_len)
        pre = ans[prehindex]  + (i - prehindex) * h
        ans.append(pre)


print(*ans[1:])