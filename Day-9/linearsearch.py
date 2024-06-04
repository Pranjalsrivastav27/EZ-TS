def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input().split()))
target=int(input())
a=linear_search(arr,target)
if a!=-1:
    print("element is found")
else:
    print("element is not found")