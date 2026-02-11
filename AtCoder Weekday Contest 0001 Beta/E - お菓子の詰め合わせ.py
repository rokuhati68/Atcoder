from collections import defaultdict
from copy import deepcopy
N, S = map(int,input().split())
A = list(map(int,input().split()))

Afirst = A[:N//2]
Asecond = A[N//2:]

firstdic = defaultdict(int)
firstdic[0] = 1

for a in Afirst:
    newdic = firstdic.copy()
    for s,cnt in firstdic.items():
        if s + a > S:
            continue
        newdic[s + a] += cnt
    firstdic = newdic

seconddic = defaultdict(int)
seconddic[0] = 1

for a in Asecond:
    newdic = seconddic.copy()
    for s,cnt in seconddic.items():
        if s + a > S:
            continue
        newdic[s + a] += cnt
    seconddic = newdic

ans = 0
for s, cnt in firstdic.items():
    if S - s in seconddic:
        ans += cnt * seconddic[S - s]

print(ans)