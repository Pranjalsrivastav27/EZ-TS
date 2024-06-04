def ispalindrome(string):
    return string==string[::-1]
def count_pal(string):
    count=0
    n=len(string)
    for i in range(n):
        for j in range(i,n):
            if ispalindrome(string[i:j+1]):
                count+=1
    return count
a="MadamMadam"
b=count_pal(a)
print(b)        