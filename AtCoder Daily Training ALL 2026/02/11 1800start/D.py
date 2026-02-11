from collections import deque
S = list(input())
q = deque(S)

cnt = 0
idx = 1
while q:
    now = q.popleft()
    if idx % 2 == 1:
        if now == "i":
            idx += 1
        else:
            idx += 2
            cnt += 1
    else:
        if now == "o":
            idx += 1
        else:
            idx += 2
            cnt += 1

if idx % 2 == 0:
    print(cnt + 1)
else:
    print(cnt)