N,M = map(int,input().split())
cnt = [1] * N
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    cnt[a] += 1
    cnt[b] += 1

ans = []
for i in cnt:
    pre = 0
    if N - i < 3:
        ans.append(0)
    else:
        pre = (N - i) * (N - i - 1) * (N - i - 2) //6
        ans.append(pre)

print(*ans)