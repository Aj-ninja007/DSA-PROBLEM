import math
def check(l):
    n=len(l)
    c=0
    for i in l:
        x=int(math.sqrt(i))
        if x*x==i:
            print(i)
            c+=1
       
    return c
l=[2,4,16,81,64,100]
print(check(l))
