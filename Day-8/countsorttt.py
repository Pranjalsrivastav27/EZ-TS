def count_sort(arr):
    a=len(arr)
    count=[0]*a
    res=[0]*a
    for i in range(a):
        count[i]+=1
    for i in range(a):
        count[i]+=count[i-1]
    n=a-1
    while n>=0:
        res[count[arr[n]]-1]=arr[n]
        count[arr[n]]-=1
        n-=1
    for i in range(0,a):
        arr[i]=res[i]
arr=list(map(int,input("enter the number").split()))
count_sort(arr)
for i in range(0,len(arr)):
    print(arr[i],end=" ")
