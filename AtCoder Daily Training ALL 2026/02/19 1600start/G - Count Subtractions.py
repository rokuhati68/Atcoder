A, B = map(int,input().split())

if A < B:
    A,B = B,A
    
ans = 0

while A != B:
    
    cnt = (A - B - 1) // B
    cnt += 1
    A -= B * cnt
    ans += cnt
    A,B = B,A

print(ans)