def selection(l):
    n=len(l)

    for i in range(n-1):
        smallest=i
        for j in range(i+1,n):
            if l[smallest]>l[j]:
                smallest=j
        temp=l[i]
        l[i]=l[smallest]
        l[smallest]=temp
    return l

l=[8,4,3,6,2]
print(selection(l))
# isme baar baar swap nhi hota ek baar jb loop chl jate h tb dubar chlte h
# time complexity= 0(n^2)