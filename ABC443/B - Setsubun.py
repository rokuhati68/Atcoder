N , K = map(int,input().split())
cnt = 0
idx = 0
while cnt < K:
    cnt += N + idx
    idx += 1

print(idx - 1)