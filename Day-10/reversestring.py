s=input()
a=list(s)
length=len(a)
start=0
end=length-1
while start<end:
    if not a[start].isalnum():
        start+=1
    elif not a[end].isalnum():
        end-=1
    else:
        a[start],a[end]=a[end],a[start]
        start+=1
        end-=1
rev="".join(a)
print(rev)
