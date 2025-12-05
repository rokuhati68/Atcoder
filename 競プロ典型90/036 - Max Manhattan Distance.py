N, Q = map(int,input().split())
_maxZ = -10**10
_minZ = 10**10
_maxW = -10**10
_minW = 10**10
l = []
for _ in range(N):
    x,y = map(int,input().split())
    _maxZ = max(_maxZ,x + y)
    _minZ = min(_minZ,x + y)
    _maxW = max(_maxW,x - y)
    _minW = min(_minW,x - y)
    l.append((x + y,x - y))
    
for _ in range(Q):
    i = int(input())-1
    z,w = l[i]
    print(max(_maxZ - z,z - _minZ,_maxW - w, w - _minW))