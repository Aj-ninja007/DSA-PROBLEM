def Negativecountwithpreviousday(l):
    n=len(l)
    count=0
    comp=l[0]
    for i in range(1,n):
        if comp>l[i]:
            print(l[i])
            count+=1
        comp=l[i]
    return count
    
       
       
l=[5,6,4,5,2,3,4]
print(Negativecountwithpreviousday(l))
