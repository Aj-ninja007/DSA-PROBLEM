
def sumofPrime(n):
    sum=0
    for i in range(2,n):
        a=True
        for j in range(2,i):
            if i%j==0:
                a=False
                break
        if a:
            sum+=i
            print(i)
        
    return sum
n=10
print(sumofPrime(n))

