from collections import deque
M = int(input())
edge = [[]for _ in range(9)]
for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)


P = list(map(int,input().split()))
st = 0
for i in range(8):
    st += 9**(P[i] - 1) * (i + 1)

dic = {st:0}
q = deque()
q.append(st)
while q:
    now = q.popleft()
    for i in range(9):
        if (now//(9**i)) % 9 == 0:
            idx = i
            break
    for to in edge[idx]:
        koma = (now // (9**to)) % 9
        nxt = now - (9**to * koma) + (9**idx * koma)
        if nxt not in dic:
            dic[nxt] = dic[now] + 1
            q.append(nxt)
goal = 0
for i in range(8):
    goal += (9 ** i) * (i + 1)

if goal not in dic:
    print(-1)
else:
    print(dic[goal])
        