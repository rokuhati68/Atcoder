from bisect import bisect_left
A, B, Q = map(int,input().split())
S = [0,1,10**30]
for _ in range(A):
    s = int(input())
    S.append(s + 10**10)
S.sort()
T = [0,1,10**30]
for _ in range(B):
    t = int(input())
    T.append(t + 10**10)
T.sort()

for _ in range(Q):
    ans = 10**30
    x = int(input())
    x += 10**10
    sidx = bisect_left(S,x)
    left_s = S[sidx - 1]
    right_s = S[sidx]
    left_t_idx = bisect_left(T,left_s)
    left_left_t = T[left_t_idx - 1]
    left_right_t = T[left_t_idx]
    ans = min(ans,x - left_left_t,x - left_s + left_right_t - left_s)
    right_t_idx = bisect_left(T,right_s)
    right_left_t = T[right_t_idx - 1]
    right_right_t = T[right_t_idx]
    ans = min(ans,right_right_t - x,right_s - x + right_s - right_left_t)
    tidx = bisect_left(T,x)
    left_t = T[tidx - 1]
    right_t = T[tidx]
    left_s_idx = bisect_left(S,left_t)
    left_left_s = S[left_s_idx - 1]
    left_right_s = S[left_s_idx]

    ans = min(ans,x - left_left_s,x - left_t + left_right_s - left_t)
    right_s_idx = bisect_left(S,right_t)
    right_left_s = S[right_s_idx - 1]
    right_right_s = S[right_s_idx]
    ans = min(ans,right_right_s - x,right_t - x + right_t - right_left_s)
    print(ans)