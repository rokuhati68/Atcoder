A,B,C,M = map(int,input().split())
R = 0
for _ in range(M):
    p,e = map(int,input().split())
    R += pow(2,e)

R = pow(R,0.5) *C

print(100**(10**5))