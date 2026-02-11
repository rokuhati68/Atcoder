from collections import deque
N, K ,X = map(int,input().split())
S = []
for _ in range(N):
    s = str(input())
    S.append(s)

ans = []

def dfs(idx, rit):
    if idx == K:
        ans.append(rit)
        return
    for i in range(N):
        nxt= rit +S[i]
        dfs(idx + 1,nxt)

dfs(0,"")
ans.sort()
print(ans[X - 1])


