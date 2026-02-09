from collections import Counter
N = int(input())
A = list(map(int,input().split()))
C = Counter(A)
S = set(A)
used = 0
up = 0
ans = []
last0 = 0
i=0
while used != N or up != 0:
    i += 1
    all = N - used + up
    up, pre = divmod(all,10)
    ans.append(str(pre))
    if str(pre) != "0":
        last0 = i
    if i in S:
        used += C[i]
ans = ans[:last0]
ans.reverse()

print("".join(ans))

    
