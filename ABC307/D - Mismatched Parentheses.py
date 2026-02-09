from collections import deque

N = int(input())
S = input()
q = deque()
cnt = 0
for i in S:
    if i == "(":
        cnt += 1
        q.append("(")
    elif i == ")":
        if cnt > 0:
            while True:
                pre = q.pop()
                if pre == "(":
                    cnt -= 1
                    break
        else:
            q.append(")")
    else:
        q.append(i)
    print(q)
print("".join(q))