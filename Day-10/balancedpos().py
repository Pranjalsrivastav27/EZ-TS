def balpos(s):
    count=0
    l=[]
    for i in s:
        if i=='[' or i=='{' or i=='(':
            l.append(i)
            count+=1
            continue
        if len(l)==0:
            return count+1
        temp=l.pop()
        if temp=='(' and i==')':
            count+=1
        elif temp=='{' and i=='}':
            count+=1
        elif temp=='[' and i==']':
            count+=1
        else:
            return count+1
    if len(l)==0:
        return 0
    else:
        return count+1
s=input()
print(balpos(s))

