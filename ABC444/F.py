from sortedcontainers import SortedList
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    s = SortedList(A)
    if(N % 2 == 0):
        mid = sum(s[N // 2] + s[(N - 1)//2])//2
    else:
        mid = s[N // 2]
