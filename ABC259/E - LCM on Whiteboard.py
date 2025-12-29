from collections import defaultdict
N = int(input())
dic = defaultdict(list)
for i in range(N):
    m = int(input())
    for _ in range(m):
        p,e = map(int,input().split())
        dic[p].append((e,i))

ans = [False] * N
for key in dic:
    v = dic[key]
    v.sort(reverse = True)
    if len(v) == 1:
        ans[v[0][1]] = True
    elif v[0][0] != v[1][0]:
        ans[v[0][1]] = True


print(min(sum(ans) + 1,N))