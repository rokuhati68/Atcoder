import math
T = int(input())

A = []
for _ in range(T):
	C,D =  [int(s) for s in input().split()]
	res = 0
	for i in range(1, math.floor(math.log10(C+D))+2):
		L = max(1, 10**(i-1) - C)
		R = min(D, 10**i - 1 - C)
		if not(L > R):
			res += math.isqrt(C*10**i+C+R) - math.isqrt(C*10**i+C+L-1)
	A.append(res)

for a in A:
	print(a)