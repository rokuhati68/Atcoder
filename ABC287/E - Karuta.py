N = int(input())
root = {}
ans = 0
S = []
for _ in range(N):
    s = input().strip()
    S.append(s)
    tree = root
    for c in s:
        if c in tree:
            ans += tree[c][0]
            tree[c][0] += 1
        else:
            tree[c] = [1,{}]
        tree = tree[c][1]

for s in S:
    tree = root
    cnt = 0
    for c in s:
        if tree[c][0] == 1:
            break
        else:
            tree = tree[c][1]
            cnt += 1
    print(cnt)
        