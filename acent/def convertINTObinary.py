
def convertINTObinary(n):
    count=0
    
    for i in range(1,n+1):
        sum=0
        t=bin(i)
        
        l=t[2:]
        
        for i in str(l):
            if int(i)==0:
                sum+=1
            if int(i)==1:
                sum+=2
        
        if sum%2!=0:   #also count odd sum 
            count+=1
    return count
                
         
        
       
    
n=4
print(convertINTObinary(n))
