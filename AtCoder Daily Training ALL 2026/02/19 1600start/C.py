N = int(input())
W = [list(input())for _ in range(N)]

for i in range(N):
    for j in range(N):
        if W[i][j] == "W":
            if W[j][i] != "L":
                print("incorrect")
                exit()
        elif W[i][j] == "L":
            if W[j][i] != "W":
                print("incorrect")
                exit()
        elif W[i][j] == "D":
            if W[j][i] != "D":
                print("incorrect")
                exit()

print("correct")