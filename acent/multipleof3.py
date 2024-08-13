def multipleof3(l):
    n=len(l)
    count=0
    comp=l[0]
    for i in l:
        if i%3==0:
            count+=1
            
    return count
l=[12,21,3,1]
print(multipleof3(l))
