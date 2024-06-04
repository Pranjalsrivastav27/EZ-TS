s=input()
los=s.split(',')
op=''
for i in los:
    a=i.split(":")
    name=a[0]
    code=a[1]
    l=len(name)
    max=0
    for i in code:
        if int(i)>=max and int(i)<=len(name):
            max=int(i)
    if max==0:
        op+='X'
    else:
        op+=name[max-1]
print(op)


