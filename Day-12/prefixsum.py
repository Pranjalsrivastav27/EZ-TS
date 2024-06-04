def prefix_sum(arr,quiries):
    n=len(arr)
    ps=[0 for i in range(n)]
    for i in range(n):
        if i==0:
            ps[i]=arr[i]
        else:
            ps[i]=ps[i-1]+arr[i]
    for query in quiries:
        i=query[0]
        j=query[1]
        if i==0:
            print(ps[j],end=" ")
        else:
            print(ps[j]-ps[j-1])
arr=list(map(int(input().split())))
quiries=int(input())
prefix_sum(arr,quiries)