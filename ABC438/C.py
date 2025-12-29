from collections import deque
N = int(input())
A = list(map(int,input().split()))
q = deque()
q.append((-1,0))
pre = A[0]
cnt = 1
for i in range(1,N):
    a = A[i]
    if a == pre:
        cnt += 1
        if cnt == 4:
            pre, cnt = q.pop()
    else:
        q.append((pre,cnt))
        pre = a
        cnt = 1
q.append((pre,cnt))

ans = 0
while q:
    pre,cnt = q.popleft()
    ans += cnt

print(ans)