from collections import defaultdict
N, K = map(int,input().split())
S = input()
MOD = 998244353

mp = {"C" * (K - 1):1}
for c in S:
    tmp = defaultdict(int)
    if c == "A":
        for s,v in mp.items():
            tmp[s + "A"] += v
    elif c == "B":
        for s,v in mp.items():
            tmp[s + "B"] += v
    else:
        for s,v in mp.items():
            tmp[s + "A"] += v
            tmp[s + "B"] += v
    mp = defaultdict(int)
    for s,v in tmp.items():
        if s != s[::-1]:
            mp[s[1:]] += v

print(sum(mp.values())% MOD)