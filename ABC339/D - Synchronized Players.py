from collections import deque,defaultdict
N = int(input())
S = []
S.append("#" * (N + 2))
for _ in range(N):
    s = input()
    s = "#" + s + "#"
    S.append(s)
S.append("#" * (N + 2))
sg = []
for i in range(N + 1):
    for j in range(N + 1):
        if S[i][j] == "P":
            sg.append((i,j))

sy, sx = sg[0]
gy, gx = sg[1]
q = deque()
q.append((sy,sx,gy,gx,0))
dic = defaultdict(lambda:10**10)
dic[(sy,sx,gy,gx)] = 0
ans = 10**10
while q:
    y1,x1,y2,x2, cost = q.popleft()
    for dy,dx in ((1,0),(0,1),(-1,0),(0,-1)):
        ty1 = y1 + dy
        tx1 = x1 + dx
        ty2 = y2 + dy
        tx2 = x2 + dx
        if S[ty1][tx1] == "#":
            ty1 = y1
            tx1 = x1
        if S[ty2][tx2] == "#":
            ty2 = y2
            tx2 = x2
        if ty1 > ty2:
            ty1,tx1,ty2,tx2 = ty2,tx2,ty1,tx1
        elif ty1 == ty2 and tx1 > tx2:
            tx1, tx2 = tx2,tx1
        elif ty1 == ty2 and tx1 == tx2:
            ans = min(ans,cost + 1)
            continue
        if dic[(ty1,tx1,ty2,tx2)] > cost + 1:
            dic[(ty1,tx1,ty2,tx2)] = cost + 1
            q.append((ty1,tx1,ty2,tx2,cost + 1))

if ans == 10**10:
    print(-1)
else:
    print(ans)