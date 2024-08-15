# def buble(l):
#     n=len(l)
    # for i in range(n):
    #     for j in range(n):
    #         if l[j]>l[i]:
    #             temp=l[j]
    #             l[j]=l[i]
    #             l[i]=temp
    # return l

# l=[8,4,3,6,2]
# print(buble(l))

# time complexity= 0(n^2)
def bubble(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l

l=[8,4,3,6,2]
print(bubble(l))