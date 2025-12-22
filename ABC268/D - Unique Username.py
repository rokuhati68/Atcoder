from itertools import permutations

N, M = map(int, input().split())
S = []
length = 0
for _ in range(N):
    s = input()
    length += len(s)
    S.append(s)

T = set(input() for _ in range(M))

def make(idx, cur, diff):
    if len(cur) > 16:
        return

    if idx == N:
        if 3 <= len(cur) <= 16 and cur not in T:
            print(cur)
            exit()
        return

    if idx > 0:
        # アンダースコアを1～diff+1個入れる
        for k in range(1, diff + 2):
            make(idx + 1, cur + "_" * k + v[idx], diff - (k - 1))
    else:
        make(idx + 1, v[idx], diff)

# アンダースコアに使える余裕
diff = 16 - (sum(len(s) for s in S) + (N - 1))

for v in permutations(S):
    make(0, "", diff)

print(-1)
