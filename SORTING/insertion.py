def insertion(l):
    n=len(l)
    for i in range(1,n):
        temp=l[i]
        j=i-1
        while j>=0 and temp<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=temp
    return l

l=[8,4,3,6,2]
print(insertion(l))

# time complexity= 0(n^2)