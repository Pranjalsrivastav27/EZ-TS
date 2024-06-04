row=6
col=6
for i in range(row):
    for j in range(col):
        if i==j or i+j==4-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()