from atcoder.dsu import DSU
from collections import deque,defaultdict
H,W, Y = map(int,input().split())
dic = defaultdict(list)
A = []
A.append([0]*(W + 2))
for i in range(H):
    al = list(map(int,input().split()))
    for j in range(W):
        a = al[j]
        dic[a].append((W + 2) * (i + 1) + j + 1)
    A.append([0] + al + [0])
A.append([0]*(W + 2))

uf = DSU((W + 2)*(H + 2))
for i in range(1,W + 2):
    uf.merge(0,i)
for j in range(1,H + 1):
    uf.merge(0,j*(W + 2))
    uf.merge(0,(j + 1)*(W + 2) - 1)
for i in range(W + 2):
    uf.merge(0,(W + 2) * (H + 1) + i)


all = (W + 2) * (H  + 2)
for i in range(1,Y + 1):
    q = deque()
    for j in dic[i]:
            isOK = False
            if uf.same(0,j - 1):
                isOK = True
                
            elif uf.same(0,j + 1):
                isOK = True
                
            elif uf.same(0,j - (W + 2)):
                isOK = True
                
            elif uf.same(0,j + (W + 2)):
                isOK = True
                
            if isOK:
                uf.merge(0,j)
                q.append(j)
    while q:
        now = q.popleft()
        h,w = divmod(now,W + 2)
        if A[h][w - 1] <= i and not uf.same(0,now - 1):
            uf.merge(0,now - 1)
            q.append(now - 1)
        if A[h][w + 1] <= i and not uf.same(0,now + 1):
            uf.merge(0,now + 1)
            q.append(now + 1)
        if A[h - 1][w] <= i and not uf.same(0,now - (W + 2)):
            uf.merge(0,now - (W + 2))
            q.append(now - (W + 2))
        if A[h + 1][w] <= i and not uf.same(0,now + (W + 2)):
            uf.merge(0,now + (W + 2))
            q.append(now + (W + 2))
    print(all - uf.size(0))


    