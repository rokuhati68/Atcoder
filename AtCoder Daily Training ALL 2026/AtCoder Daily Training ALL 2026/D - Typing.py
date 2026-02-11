S = input().strip()
T = input().strip()

idx = 0
for i in range(len(T)):
    if T[i] == S[idx]:
        print(i + 1, end = " ")
        idx += 1