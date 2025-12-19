N=int(input()) 
A=list(map(int,input().split()))
B=list(map(int,input().split())) 
L=[0] 
for i in range(N-1):
    if B[i]>0:
        L.append(i+1)
ans=0
for i in range(len(L)-1):
    s=L[i+1]
    d=L[i]
    r=s
    l=s-A[s-1]
    ans+=1
    if l<=d:
        continue
    f=10**18
    while f>d:
        for j in range(l,s):
            f=min(f,j-A[j-1])
        s=l
        l=f
        ans+=1
print(ans)
    

    


    