import sys
sys.setrecursionlimit(10**8)
T = int(input())
def check(left,right,_len):
    
    if _len >= 1:
        left = check(left[:1<<(_len - 1)],left[1<<(_len - 1):],_len - 1)
        right = check(right[:1 <<(_len - 1)],right[1<<(_len - 1):],_len - 1)
    if left[0] > right[0]:
        left,right = right,left
    return left + right
    



for _ in range(T):
    N = int(input())
    P = list(map(int,input().split()))
    print(*check(P[:1 << (N - 1)],P[1 << (N - 1):],N - 1))
    