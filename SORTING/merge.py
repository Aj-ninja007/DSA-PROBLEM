# time complexity->o(nlogn)



# def mergesort(arr,l,h):
#     if l<h:
#         mid=(l+h)//2
       
#         mergesort(arr,l,mid)
#         print(arr,l,mid)
#         mergesort(arr,mid+1,h)
#         merge(arr,l,mid,h)
#     return arr

# def merge(arr,l,mid,h):
#     b=[]
#     i=l
#     j=mid+1
#     while i<=mid and j<=h:
#         if arr[i]<arr[j]:
#             b.append(arr[i])
#             i+=1
#         else:
#             b.append(arr[j])
#             j+=1
#     if i>mid:
#         while j<=h:
#             b.append(arr[j])
#             j+=1
#     else:
#         while i<=mid:
#             b.append(arr[i])
#             i+=1
#     print(b)  
#     for i in range(len(b)):
#         arr[l+i]=b[i]
#     return arr

# l=[8,4,3,6,2,1]
# n=len(l)
# print(mergesort(l,0,n-1))


# or



def mergesort(arr, l, h):
    if l < h:
        mid = (l + h) // 2
        mergesort(arr, l, mid)
        mergesort(arr, mid + 1, h)
        merge(arr, l, mid, h)
    return arr

def merge(arr, l, mid, h):
    b = []
    i = l
    j = mid + 1
    while i <= mid and j <= h:
        if arr[i] < arr[j]:
            b.append(arr[i])
            i += 1
        else:
            b.append(arr[j])
            j += 1
    while i <= mid:
        b.append(arr[i])
        i += 1
    while j <= h:
        b.append(arr[j])
        j += 1
       
    for i in range(len(b)):
        arr[l + i] = b[i]  # Correctly update the original array in the specified range
    return arr

l = [8, 4, 3, 6, 2, 1]
n = len(l)
print(mergesort(l, 0, n - 1))
