class A:
    x = input("enter the string")
    y=int(input("enter the first number"))
    z=int(input("enter the second number"))
    def add(self,a,b):
        print(a[::-1])
        print((b*b))
    def display_results(self,x,y,z):
        print(len(x))
        print(y%z)
obj=A()
obj.add(obj.x,obj.y)
obj.display_results(obj.x,obj.y,obj.z)