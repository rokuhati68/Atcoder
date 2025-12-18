import sys
sys.setrecursionlimit(10**8)
H, W, A, B = map(int,input().split())

def check(a,b,S):
    global ans
    if a == 0 and b == 0:
        ans += 1
    for i in range(H * W):
        if i not in S:
            ny,nx = divmod(i,W)
            break
    if a > 0:
        if nx != W - 1 and i + 1 not in S:
            check(a - 1,b,S|{i,i + 1})
        if ny != H - 1:
            check(a - 1,b,S|{i,i + W})
    if  b> 0:
        check(a,b - 1,S|{i})
    
ans = 0
check(A,B,set())
print(ans)