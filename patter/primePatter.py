

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    print()
    return primes
    

def print_prime_pattern(n):
    primes = generate_primes(n - 2)  # Adjust to account for the inclusion of 1
    print(primes)
    sequence = [1]  # Start with 1
    for i in range(len(primes) + 1):
        print("".join(map(str, sequence)))
        if i < len(primes):
            sequence.append(primes[i])

# Print the pattern with the first 5 numbers including 1
print_prime_pattern(5)









def pattern():
    n=5
    for i in range(n-1):
        for j in range(i+1):
            print("*",end=" ")
        print(" ")
pattern()
def pattern():
    n=5
    for i in range(n,0,-1):
                                        
        for k in range(i-1):
            print("*",end=" ")
        print(" ")
pattern()
* * * *  
* * *  
* *  
*  
            
def pattern():
    n=5
    for i in range(1,n+1):
        for k in range(n-i):
            print(" ",end=" ")
        for j in range(1,2*i):
            print("*",end=" ")
        print(" ")
    for i in range(n-1,0,-1):
        for k in range(n-i):
            print(" ",end=" ")
        for j in range(1,2*i):
            print("*",end=" ")
        print(" ")
            
pattern()


        *  
      * * *  
    * * * * *  
  * * * * * * *  
* * * * * * * * *  
* * * * * * * * *  
  * * * * * * *                  
    * * * * *  
      * * *  
        *  





        *  
      * * *  
    * * * * *  
  * * * * * * *  
* * * * * * * * *  
  * * * * * * *  
    * * * * *  
      * * *  
        *  
            
            
# def pater():
#     n=5
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print(" ",end=" ")
#         for k in range(1,2*i):
#             print("*",end=" ")
#         print( )
#     for i in range(n-1,0,-1):
#         for j in range(n-i):
#             print(" ",end=" ")
#         for k in range(1,2*i):
#             print("*",end=" ")
#         print( )
        
        
# pater()

# def second(l):
#     lar=0
#     s=0
#     lar=l[0]
#     for i in range(1,len(l)):
#         if l[i]>lar:
#             lar=l[i]
#     for i in range(len(l)):
#         if l[i]>s and l[i]!=lar:
#             s=l[i]
#     return s
# l=[4,3,6,2,8,9]
# print(second(l))

def second(l):
    lar=0
    s=0
    lar=l[0]
    for i in range(1,len(l)):           #optmised approach
        if l[i]>lar:
            s=lar
            lar=l[i]
        elif lar>l[i] and l[i]>s:
            s=l[i]
    return s
l=[4,3,6,2,8,9]
print(second(l))

    





























        
