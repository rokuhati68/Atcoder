N = int(input())
l = []

cnt = 0
for _ in range(N):
    s = input().strip()
    cnt = max(cnt,len(s))
    l.append(s)

for i in l:
    _len = len(i)
    _len = cnt - _len
    print("."*(_len//2) + i + "."*(_len//2))