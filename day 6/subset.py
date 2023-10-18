a = [6,8,9,5,4,3,26,2]
b =[]
result =[]
c=[]
sum =0
target=28
for i in a:
    if(sum<=28):
        sum=sum+i
        if(sum<=28):
            b.append(i)

result = [x for x in a if x not in b]
k=0
for i in result:
    if(k<=28):
        k=k+i
        if(k<=28):
            c.append(i)

print(b)
print(c)


