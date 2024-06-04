n=9
col=2*n-1
start,end=n-1,n-1
for i in range(0,n,1):
    for j in range(col):
        if j>=start and j<=end: 
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
    start-=1
    end+=1

