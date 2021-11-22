def heapify(arr,n,i):
    root = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[root][0] > arr[l][0]:
        root = l
    if r < n and arr[root][0] > arr[r][0]:
        root = r
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr,n,root)

def buildHeap(arr, n): 
    startIdx = n // 2 - 1 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i) 

def insertToHeap(arr,val):
    n = len(arr)
    arr[-1] = val
    n -= 1 
    while n > 0 and arr[(n-1)//2][0] > arr[n][0]:
        arr[n], arr[(n-1)//2] = arr[(n-1)//2], arr[n]
        n = (n-1)//2

def popRootFromHeap(arr):
    arr[0] = arr[-1]
    arr[-1] = (float("inf"),None)
    heapify(arr,len(arr),0)

def mergeSortedLists():
    n,k = map(int,input().split())
    arr = [None]*k
    for i in range(k):
        arr[i] = list(map(int,input().split(",")))
    new = [None]*n
    heap = [None]*k
    for i in range(k):
        heap[i] = (arr[i][0],i)
    buildHeap(heap,k)
    for i in range(n):
        new[i] = heap[0][0]
        x = heap[0][1]
        popRootFromHeap(heap)
        arr[x].pop(0)
        if len(arr[x]) > 0:
            insertToHeap(heap,(arr[x][0],x))
    print(new)

mergeSortedLists()
