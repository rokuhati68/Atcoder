N = int(input())
S = input()

def check(dp):
    for i in range(1,N):
        if S[i] == "o" and dp[i] == 0:
            dp[i + 1] = dp[i - 1]
        elif S[i] == "x" and dp[i] == 0:
            dp[i + 1] = (dp[i - 1] + 1) %2
        elif S[i] == "o" and dp[i] == 1:
            dp[i + 1] = (dp[i - 1] + 1) % 2
        elif S[i] == "x" and dp[i] == 1:
            dp[i + 1] = dp[i - 1]
    

for i in range(2):
    for j in range(2):
        dp = [-1] * (N + 1)
        dp[0] = i
        dp[1] = j
        check(dp)
        if dp[0] != dp[-1]:
            continue
        isOK = True
        if S[0] == "o" and dp[0] == 0:
            if dp[1] != dp[-2]:
                isOK = False
        elif S[0] == "o" and dp[0] == 1:
            if dp[1] == dp[-2]:
                isOK = False
        elif S[0] == "x" and dp[0] == 0:
            if dp[1] == dp[-2]:
                isOK = False
        elif S[0] == "x" and dp[0] == 1:
            if dp[1] != dp[-2]:
                isOK = False
        if isOK:
            for i in range(N):
                if dp[i] == 0:
                    print("S",end="")
                else:
                    print("W",end="")
            exit()

print(-1)