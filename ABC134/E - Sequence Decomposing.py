from sortedcontainers import SortedList
N = int(input())
st = SortedList()
for _ in range(N):
    a = int(input())
    idx = st.bisect_left(a)
    if idx == 0:
        st.add(a)
    else:
        st.pop(idx - 1)
        st.add(a)

print(len(st))