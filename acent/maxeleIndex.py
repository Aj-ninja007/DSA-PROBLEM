import math
def check(l):
    n=len(l)
    maxi=0
    j=-1
    for i ,num in enumerate(l):
        if num>maxi:
            maxi=num
            j=i
    return [maxi,j]
       
       
l=[90,100,30,102,80,70,101]
print(check(l))
