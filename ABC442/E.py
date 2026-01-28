import math
from collections import defaultdict
from functools import cmp_to_key

N, Q = map(int, input().split())
# XY = []
d = defaultdict(int)
didx = defaultdict(list)

for i in range(N):
    xi, yi = map(int, input().split())

    if xi == 0:
        yi //= abs(yi)
    elif yi == 0:
        xi //= abs(xi)
    else:
        g = math.gcd(abs(xi), abs(yi))
        xi //= g
        yi //= g
    
    # XY.append((xi, yi, i))
    d[(xi, yi)] += 1
    didx[(xi, yi)].append(i)

# XYs = sorted(d.keys(), key=lambda x: -math.atan2(x[1], x[0]))

def comp(a, b):
    v = a[0] * b[1] - a[1] * b[0]

    if v > 0:
        return 1
    elif v < 0:
        return -1
    else:
        return 0
    
XYs = sorted([t for t in d.keys() if t[1] > 0 or t == (1, 0)], key=cmp_to_key(comp))
XYs += sorted([t for t in d.keys() if t[1] < 0 or t == (-1, 0)], key=cmp_to_key(comp))


# for i in range(len(XYs)-1):
    # x1, y1 = XYs[i]
    # x0, y0 = XYs[i+1]
# 
    # if x0 * y1 - y0 * x1 > 0:
        # pass
    # else:
        # XYs[i], XYs[i+1] = XYs[i+1], XYs[i]


# print(d)
# print(didx)
# print(XYs)

conv = [0] * N
for i in range(len(XYs)):
    for j in didx[XYs[i]]:
        conv[j] = i

# print(conv)

XYs *= 2

acc = [0]
val = 0

for t in XYs:
    val += d[t]
    acc.append(val)

# print(XYs)
# print(acc)

for _ in range(Q):
    ai, bi = map(lambda x:int(x)-1, input().split())

    aic = conv[ai]
    bic = conv[bi]

    # print(aic, bic)

    if aic <= bic:
        pass
    else:
        bic += len(d.keys())

    # print(aic, bic)

    ans = acc[bic+1] - acc[aic]

    print(ans)
    # print("")
