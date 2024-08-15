# # time complexity-O(n*log(n)



# def partion(arr,l,h):
#     pivet=arr[l]
#     i=l
#     j=h
#     while i<j:
#         while pivet>=arr[i]:
#             i+=1
#         while pivet<arr[j]:
#             j-=1
#         if i<j:
#             swap(arr,i,j)
#     swap(arr,j,l)
#     return i


# def swap(arr,i,j):
#     temp=arr[i]
#     arr[i]=arr[j]
#     arr[j]=temp
#     return arr

# def quick(arr,l,h):
#     if l<h:
#         p=partion(arr,l,h)
#         quick(arr,l,p-1)
#         quick(arr,p+1,h)
#     return arr

# l=[8,4,3,6,2]
# n=len(l)-1
# print(quick(l,0,n))



def quick(arr, l, h):
    if l < h:
        p = partition(arr, l, h)
        quick(arr, l, p - 1)
        quick(arr, p + 1, h)
    return arr

def partition(arr, l, h):
    pivot = arr[l]
    i = l
    j = h
    
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            swap(arr, i, j)
        else:
            break
    
    swap(arr, l, j)
    return j

def swap(arr, i, j):
    # arr[i], arr[j] = arr[j], arr[i]
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

    return arr

l = [8, 4, 3, 6, 2]
n = len(l) - 1
print(quick(l, 0, n))
