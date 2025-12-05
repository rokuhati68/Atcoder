N,K = map(int,input().split())
S = list(input())
nex = [[N + 1] * 26 for _ in range(N + 1)]

for i in range(N - 1, - 1, -1):
    for j in range(26):
        nex[i][j] = nex[i + 1][j]
    
    nex[i][ord(S[i]) - ord("a")] = i

ans = []
st = 0
for i in range(K):
    for j in range(26):
        idx = nex[st][j]
        if K - i <= N - idx:
            ans.append(chr(ord("a") + j))
            st = idx + 1
            break

print("".join(ans))