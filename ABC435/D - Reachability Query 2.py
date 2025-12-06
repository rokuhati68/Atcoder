from collections import deque
N, M = map(int,input().split())
edge = [[]for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    edge[y].append(x)
s = set()
Q = int(input())
for _ in range(Q):
    q,v = map(int,input().split())
    v -= 1
    if q == 1:
        if v in s:
            continue
        dq = deque()
        dq.append(v)
        s.add(v)
        while dq:
            now = dq.popleft()
            for to in edge[now]:
                if to in s:
                    continue
                s.add(to)
                dq.append(to)
    else:
        if v in s:
            print("Yes")
        else:
            print("No")