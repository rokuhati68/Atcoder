N, M = map(int,input().split())
l = []
for _ in range(N):
    x,y,z = map(int,input().split())
    l.append((x,y,z))

ans = 0
for i in range(-1,2):
    if i==0:continue
    for j in range(-1,2):
        if j==2:continue
        for r in range(-1,2):
            ll=[]
            for x,y,z in l:
                ll.append(i*x+j*y+r*z)
            ll.sort(reverse = True)
            ans = max(ans,sum(ll[:M]))

print(ans)