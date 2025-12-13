from itertools import permutations
from collections import defaultdict
S = set()
alf = []
for i in range(3):
    a = input()
    for j in a:
        S.add(j)
    alf.append(list(a))
if len(S) > 10:
    print("UNSOLVABLE")
    exit()

def make(a):
    now = 0
    if dic[a[0]] == 0:
        return 0
    for i in a:
        now*= 10
        now += dic[i]
    return now

S = list(S)
_len = len(S)
l = [i for i in range(10)]
for V in permutations(l,_len):
    dic = defaultdict()
    
    for s,v in zip(S,V):
        dic[s] = v
    num1 = make(alf[0])
    num2 = make(alf[1])
    num3 = make(alf[2])
    if num1 == 0 or num2 == 0 or num3 == 0:
        continue
    if num1 + num2 == num3:
        print(num1)
        print(num2)
        print(num3)
        exit()

print("UNSOLVABLE")