def pointer_approach(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==target:
            return[left,right]
        elif sum>=target:
            right-=1
        else:
            left+=1
    return []
arr=list(map(int,input("enter the elements").split()))
target=int(input("enter the number"))
res=pointer_approach(arr,target)
print(res)
