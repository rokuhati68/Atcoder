from itertools import permutations,product
N = int(input())
R = input()
C = input()

l = [i for i in range(N)]
cand = [[]for _ in range(N)]
for i in range(N):
    for a,b,c in permutations(l,3):
        can = ["."] * N
        if R[i] == "A":
            if min(a,b,c) != a:
                continue
        elif R[i] == "B":
            if min(a,b,c) != b:
                continue
        elif R[i] == "C":
            if min(a,b,c) != c:
                continue
        can[a] = "A"
        can[b] = "B"
        can[c] = "C"
        cand[i].append(can)

for v in product(*cand):
    isOK = True
    for i in range(N):
        l = [0,0,0]
        first = "."
        for j in range(N):
            now = v[j][i]
            if first == ".":
                first = now
            if now == "A":
                l[0] += 1
            elif now == "B":
                l[1] += 1
            elif now == "C":
                l[2] += 1
        if l != [1,1,1]:
            isOK = False
            break
        if first != C[i]:
            isOK = False
            break
    if isOK:
        print("Yes")
        for i in v:
            print("".join(i))
        exit()

print("No")