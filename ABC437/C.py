T = int(input())
for _ in range(T):
    N = int(input())
    l = []
    totalweight = 0
    for _ in range(N):
        w,p = map(int,input().split())
        l.append((-(p+w)))
        totalweight += w
    l.sort()
    isOK = True
    for i in range(N):
        pw = l[i]
        pw *= -1
        totalweight -= pw
        if totalweight <= 0:
            print(N - i - 1)
            isOK = False
            break
    if isOK:
        print(0)
        
    