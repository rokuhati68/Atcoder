Ha,Wa = map(int,input().split())
A = [input()for _ in range(Ha)]
sA = set()
for i in range(Ha):
    for j in range(Wa):
        if A[i][j] == "#":
            sA.add((i,j))
Hb,Wb = map(int,input().split())
B = [input()for _ in range(Hb)]
sB = set()
for i in range(Hb):
    for j in range(Wb):
        if B[i][j] == "#":
            sB.add((i,j))
Hx,Wx = map(int,input().split())
X = [input()for _ in range(Hx)]
sX = set()
for i in range(Hx):
    for j in range(Wx):
        if X[i][j] == "#":
            sX.add((i,j))
SA= []
for ha in range(20):
    for wa in range(20):
        s = set()
        for i,j in sA:
            s.add((i + ha,j + wa))
        SA.append(s)
SB= []
for ha in range(20):
    for wa in range(20):
        s = set()
        for i,j in sB:
            s.add((i + ha,j + wa))
        SB.append(s)
        
sx = set()
for i,j in sX:
    sx.add((i + 10,j + 10))


for a in SA:
    for b in SB:
        ss = a | b
        if ss == sx:
            print("Yes")
            exit()
print("No")