from heapq import heappop,heappush
T = int(input())

for _ in range(T):
    N, H = map(int,input().split())
    q = []
    for _ in range(N):
        t,l,u = map(int,input().split())
        heappush(q,(t,l,u))
    
    _minH = H
    _maxH = H
    pret = 0
    isOK = True
    while q:
        t,l,u = heappop(q)
        time = t - pret
        canMax = _maxH + time
        canMin = max(_minH - time,1)
        if l > canMax:
            print("No")
            isOK = False
            break
        elif canMin > u:
            print("No")
            isOK = False
            break
        else:
            _maxH = min(canMax,u)
            _minH = max(canMin,l)
        pret = t
    if isOK:
        print("Yes")