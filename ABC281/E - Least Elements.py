from sortedcontainers import SortedList
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
st = SortedList(A[:M])
ans = []
_sum = sum(st[:K])
ans.append(_sum)
for i in range(N - M):
    _maxK = st[K - 1]
    remove_a= A[i]
    st.discard(A[i])
    add_a = A[i + M]
    if remove_a <= _maxK:
        _sum -= remove_a
        st.add(add_a)
        if add_a < _maxK:
            _sum += add_a
        else:
            _sum += st[K - 1]
    else:
        st.add(add_a)
        if add_a < _maxK:
            _sum -= _maxK
            _sum += add_a
    ans.append(_sum)

print(*ans)
    
    
