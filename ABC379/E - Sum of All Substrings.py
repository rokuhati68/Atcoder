n = int(input())
s = input()
a = [(i + 1) * int(s[i]) for i in range(n)]
for i in range(1, n):
    a[i] += a[i - 1]
i = 0
c = 0
ans = []
while i < n or c > 0:
    if i < n:
        c += a[n - 1 - i]
    ans.append(c % 10)
    c //= 10
    i += 1
print(*ans[::-1], sep="")

