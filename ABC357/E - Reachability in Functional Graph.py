from atcoder.scc import SCCGraph
from collections import deque,defaultdict
N = int(input())
scc = SCCGraph(N)
A = list(map(int,input().split()))
revedge = [[]for _ in range(N)]
for i in range(N):
    a = A[i]
    scc.add_edge(i,a - 1)
    revedge[a - 1].append(i)

ans = 0
s = set()
q = deque()
dic = defaultdict(int)
for v in scc.scc():
    if len(v) == 1:
        num = v[0]
        if A[num] == num + 1:
            ans += 1
            s.add(num)
            dic[num] = 1
            for to in revedge[num]:
                q.append(to)
    else:
        _len= len(v)
        ans += _len * _len
        for now in v:
            s.add(now)
            dic[now] = _len
            for to in revedge[now]:
                q.append(to)

while q:
    now = q.popleft()
    if now in s:
        continue
    preans = dic[A[now] - 1] + 1
    ans += preans
    s.add(now)
    dic[now] = preans 
    for to in revedge[now]:
        q.append(to)
    

print(ans)