N = int(input())
A = list(map(int,input().split()))
prime = [True] * (10**5 + 1)
prime[0] = False
prime[1] = False

for i in range(2,10**5 + 1):
    if prime[i]:
        for to in range(i + i,10**5 + 1,i):
            prime[to] = False

cnt = 0
for i in A:
    if prime[i]:
        cnt += 1

if cnt % 2 == 0 and N:
    print("Bruno")
else:
    print("Anna")