N, Q = map(int,input().split())
ans = 1
MOD = 10**9 + 7
l = []
for _ in range(Q):
    x,y,z,w = map(int,input().split())
    x -= 1
    y -= 1
    z -= 1
    l.append((x,y,z,w))
    
for i in range(60):
    cnt = 0
    for b in range(2**N):
        isOK = True
        for x,y,z,w in l:
            bw = (w>>i)& 1
            bx = (b>>x)& 1
            by = (b>>y)& 1
            bz = (b>>z)& 1 
            if (bx|by|bz) != bw:
                isOK = False
                break
        if isOK:
            cnt += 1
            cnt %= MOD
    ans *= cnt
    ans %= MOD

print(ans)
