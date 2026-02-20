from collections import defaultdict 
H,W, N = map(int,input().split())

dicH = defaultdict(list)
dicW = defaultdict(list)
l = []
for i in range(N):
    h,w = map(int,input().split())
    dicH[h].append(i)
    dicW[w].append(i)
    l.append((h,w))

used = set()
ansH = [0]*N
ansW = [0] * N
for _ in range(N):
    isOK = True
    while isOK:
        if len(dicH[H]) != 0:
            
            idx = dicH[H].pop()
            if idx in used:
                continue
            h,w = l[idx]
            W -= w
            ansH[idx]=1
            ansW[idx] = W + 1
            used.add(idx)
            isOK = False
        else:
            idx = dicW[W].pop()
            if idx in used:
                continue
            h,w = l[idx]
            H -= h
            ansH[idx] = H + 1
            ansW[idx] = 1
            used.add(idx)
            isOK = False
for i in range(N):
    print(ansH[i],ansW[i])
