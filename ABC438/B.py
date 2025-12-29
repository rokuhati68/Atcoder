N ,M = map(int,input().split())
S = input()
T = input()

allans = 10**10
for i in range(N - M + 1):
    ans = 0
    for j in range(M):
        if int(S[i + j]) > int(T[j]):
            ans += int(S[i + j]) - int(T[j])
        elif int(S[i + j]) < int(T[j]):
            ans += 10 + int(S[i + j]) - int(T[j])
    allans = min(allans,ans)

print(allans)