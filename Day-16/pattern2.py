n=int(input())
char='a'
for i in range(1,n+1):
    for j in range(i):
        print(char,end=" ")
        char=chr(ord(char)+1)
        if char>'z':
            char='a'
    print()