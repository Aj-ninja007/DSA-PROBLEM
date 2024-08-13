
def binaryTOdecimal(n):
    t=bin(n)
    l=list(t[2:])
    l.sort()
    x=l[::-1]
    sum=0
    for i in range(len(x)):
        if int(x[i])==1:
            sum+=2**i
    return sum
    
n=2
print(binaryTOdecimal(n))

