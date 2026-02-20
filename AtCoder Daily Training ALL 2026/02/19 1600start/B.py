N = int(input())
W  = list(map(str,input().split()))

isOK = False
for i in ("and", "not", "that", "the", "you" ):
    if i in W:
        isOK = True

if isOK:
    print("Yes")
else:
    print("No")