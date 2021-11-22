def heapify(arr,n,i):
    root = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[root] < arr[l]:
        root = l
    if r < n and arr[root] < arr[r]:
        root = r
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr,n,root)
    
# def heapSort(arr):
#     n = len(arr)
#     for i in range(n//2 -1,-1,-1):
#         heapify(arr,n,i)
    
#     for i in range(n-1,0,-1):
#         arr[i],arr[0] = arr[0],arr[i]
#         heapify(arr,i,0)

def buildHeap(arr, n): 
    startIdx = n // 2 - 1 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i) 


def insertToHeap(arr,val):
    n = len(arr)
    new = [None]*(n+1)
    for i in range(n):
        new[i] = arr[i]
    new[n] = val
    while n > 0 and new[(n-1)//2] < new[n]:
        new[n], new[(n-1)//2] = new[(n-1)//2], new[n]
        n = (n-1)//2
    return new

arr = [12, 11, 13, 5, 6, 7]
buildHeap(arr,len(arr))
new = insertToHeap(arr,30)
print(new)