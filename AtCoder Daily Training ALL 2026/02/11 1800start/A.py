N = int(input())
l = []
for _ in range(N):
    a = str(input())
    l.append(a)

for i in l[::-1]:
    print(i)
