from collections import Counter
N = int(input())
A = list(map(int,input().split()))

cnt0 = 0
l = []
for a in A:
    if a == 0:
        cnt0 += 1
        continue
    for i in range(2,int(a ** 0.5 )+ 1):
        while a % (i * i) == 0:
            a //= (i * i)
    l.append(a)


C = Counter(l)
ans = 0
ans += cnt0 * (cnt0 - 1) // 2
ans += cnt0 * (N - cnt0)


for key,value in C.items():
    ans += value*(value - 1)//2

print(ans)