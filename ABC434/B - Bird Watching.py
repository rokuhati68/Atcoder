N,M = map(int,input().split())

weight = [0] * M
cnt = [0] * M

for _ in range(N):
    a,b = map(int,input().split())
    a -= 1
    weight[a] += b
    cnt[a] += 1

for i in range(M):
    w = weight[i]
    c = cnt[i]
    print(w/c)