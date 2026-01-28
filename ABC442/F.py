N = int(input())

nowdp = [0] * (N + 1)
INF = 10**30
for i in range(N):
    S = input().strip()
    whiteCnt = [0] * (N + 1)
    blackCnt = [0] * (N + 1)
    for j in range(N):
        whiteCnt[j + 1] += whiteCnt[j]
        blackCnt[j + 1] += blackCnt[j]
        if S[j] == ".":
            whiteCnt[j + 1] += 1
        else:
            blackCnt[j + 1] += 1
    nxtdp = [INF] * (N + 1)
    _min = nowdp[-1]
    for j in range(j + 1,-1,-1):
        _min = min(_min,nowdp[j])
        changeWhite = blackCnt[j]
        changeBlack = whiteCnt[-1] - whiteCnt[j]
        nxtdp[j] = _min + changeWhite + changeBlack
    nowdp = nxtdp
    
print(min(nowdp))
        
    