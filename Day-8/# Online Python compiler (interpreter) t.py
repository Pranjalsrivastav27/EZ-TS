# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
row=int(input())
col=int(input())
mat=[]
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input("enter the number")))
    mat.append(a)
    print()
for i in range(row):
    for j in range(col):
        print(mat[i][j],end=" ")
    print()
print(mat)