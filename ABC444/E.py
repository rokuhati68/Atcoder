from sortedcontainers import SortedList
from collections import deque
N, D = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
s = SortedList()
s.add(-10**10)
s.add(10**10)

q = deque()

cnt = 0
for a in A:
    isCheck = True
    while isCheck:
        idx = s.bisect_left(a)
        if a - s[idx-1] >=D and s[idx] - a >= D:
            break
        pre = q.popleft()
        cnt -= 1
        s.remove(pre)
    cnt += 1
    ans += cnt
    q.append(a)
    s.add(a)
    
print(ans)
                
                