from collections import defaultdict
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    nonUse = set()
    for i in range(2 *N - 1):
        if A[i] == A[i + 1]:
            nonUse.add(i)
            nonUse.add(i + 1)
    
    dic = defaultdict(int)
    ans = 0
    for i in range(2 * N - 1):
        if i in nonUse:
            continue
        a = A[i]
        b = A[i + 1]
        if a in dic:
            if dic[a] == b:
                ans += 1
        dic[a] = b
    
    dic = defaultdict(int)
    for i in range(2 * N + 1):
        if i in nonUse:
            continue
        a = A[i]
        b = A[i + 1]
        