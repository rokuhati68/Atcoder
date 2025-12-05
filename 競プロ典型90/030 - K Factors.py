
N,K = map(int,input().split())
if K == 1:
    print(N - 1)
    exit()
prime = [True] * (N + 1)
cnt = [0] * (N + 1)

ans = 0
for i in range(2,N + 1):
    if cnt[i] >= K:
        ans += 1
    if prime[i] == False:
        continue
    for j in range(i + i,N + 1, i):
        cnt[j] += 1
        prime[j] = False

print(ans)




