N = int(input())
T = list(map(int,input().split()))
TT = sorted(T)
ans = []
for i in range(3):
    t = TT[i]
    ans.append(T.index(t) + 1)

print(*ans)