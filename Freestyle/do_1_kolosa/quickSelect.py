def swap(arr, a, b): 
	temp = arr[a] 
	arr[a] = arr[b] 
	arr[b] = temp 

def partition(arr, l, h):
    pivot = arr[h]
    i = l
    for j in range(l, h):
        if arr[j] <= pivot:
            swap(arr,i,j)
            i += 1
    swap(arr,i,h)
    return i

def quickSelect(arr,l,h,k):
    if k < 0:
        return
    if l == h:
        return arr[l]
    q = partition(arr,l,h)
    if q == k:
        return arr[q]
    elif k < q:
        return quickSelect(arr,l,q-1,k)
    else:
        return quickSelect(arr,q+1,h,k)

arr = [5,8,1,2,19]
print(quickSelect(arr,0,len(arr)-1,2))