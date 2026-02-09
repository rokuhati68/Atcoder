N, K = map(int,input().split())
S = []
for _ in range(N):
    l = [0] * 26
    s = input().strip()
    for  i in s:
        idx = ord(i) - ord("a")
        l[idx] = 1
    S.append(l)

ans = 0
for b in range(1<<N):
    cnt = [0] * 26
    pre = 0
    for i in range(N):
        if b >> i & 1 == 1:
            for j in range(26):
                if S[i][j]:
                    cnt[j] += 1
    for j in range(26):
        if cnt[j] == K:
            pre += 1
    ans = max(ans,pre)

print(ans)