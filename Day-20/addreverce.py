l1=[1,2,3]
l2=[4,5,6]
a="".join(str(i) for i in l1[::-1])
b="".join(str(i) for i in l2[::-1])
c=int(a)+int(b)
c=str(c)
c=c[::-1]
v=[int(i) for i in c]
print(v)
    