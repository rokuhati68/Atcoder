Q = int(input())
ans = 0
isOK = False
for _ in range(Q):
    a = int(input())
    if a == 1:
        ans += 1
    elif a == 2:
        ans = max(0,ans - 1)
    elif a == 3:
        if isOK:
            isOK = False
        else:
            isOK = True

    if(ans >= 3 and isOK):
        print("Yes")
    else:
        print("No")