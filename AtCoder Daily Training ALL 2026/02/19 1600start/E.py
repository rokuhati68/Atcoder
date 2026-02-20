from itertools import permutations 
N, M = map(int,input().split())

AB = [[]for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    AB[a].append(b)
    AB[b].append(a)

for i in AB:
    i.sort()
    
CD= [[]for _ in range(N)]
for _ in range(M):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    CD[c].append(d)
    CD[d].append(c)


for v in permutations(list(range(N))):
    cd = [[]for _ in range(N)]
    for i in range(N):
        for j in CD[v[i]]:
            cd[i].append(v[j])
    for i in cd:
        i.sort()
    if cd == AB:
        print("Yes")
        exit()
    
print("No")    
        