N,M = map(int,input().split())
S = set(input())
T = set(input())
Q = int(input())
for _ in range(Q):
    w = input()
    isS = True
    isT = True
    for i in w:
        if i not in S:
            isS = False
        if i not in T:
            isT = False
    if isS == True and isT == False:
        print("Takahashi")
    elif isS == False and isT == True:
        print("Aoki")
    else:
        print("Unknown")
