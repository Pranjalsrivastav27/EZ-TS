v=input()
s=v.split(",")
for i in range(0,len(s)):
    s[i]=int(s[i])
sum2=''
sum=0
for i in range(len(s)):
    if s[i]==4:
        index=i
    if s[i]==7:
        index1=i
for i in range(0,index):
    sum+=s[i]
for i in range(index1+1,len(s)):
    sum+=s[i]
for i in range(index,index1+1):
    sum2+=str(s[i])
print(sum+int(sum2))




    
