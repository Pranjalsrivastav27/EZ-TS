a=int(input())
arr=list(map(int,input().split(" ")))
b=[]
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
for i in range(1,len(arr)+1):
    if i not in arr:
        b.append(i)
print(b)

