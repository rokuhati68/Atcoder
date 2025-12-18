from math import gcd
from collections import defaultdict
N=int(input())
C=[tuple(map(int,input().split())) for _ in range(N)]
#from random import randint;N=2000;C=[(randint(0,10**7),randint(0,10**7)) for _ in range(N)]
#傾きとベクトルごとにカウント
DS=defaultdict(int)
DV=defaultdict(int)
for i in range(N-1):
  for j in range(i+1,N):
    x=C[j][0]-C[i][0]
    y=C[j][1]-C[i][1]
    if x<0:
      x*=-1;y*=-1
    if x==0 and y<0:
      y*=-1
    DV[(x,y)]+=1
    g=gcd(x,y)
    DS[(x//g,y//g)]+=1
#平行線2組をカウント、その後平行四辺形の重複を除く
a=sum(v*(v-1)//2 for v in DS.values())
b=sum(v*(v-1)//2 for v in DV.values())
print(a-b//2)