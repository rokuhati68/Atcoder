from collections import defaultdict
N,L,R = map(int,input().split())
P = list(map(int,input().split()))
dic = defaultdict(list)
s = set()
for i in range(N):
    p = P[i]
    dic[p].append(i)
    s.add(p)

s = list(s)
s.sort(reverse = True)

for i in s:
    if L <= i <= R:
        print(min(dic[i]) + 1)
        exit()

print(-1)
