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

def getMedian(arr):
#zwraca medianę listy
    n = len(arr)
    if n == 0: return -1
    if n == 1: return arr[0]
    if arr[0] < arr[1]:    
        minHeap = [arr[1]]
        maxHeap = [arr[0]]
    else:
        minHeap = [arr[0]]
        maxHeap = [arr[1]]
    for i in range(2,n):
        if i % 2 == 0:
            maxHeap = insertToHeap(maxHeap,arr[i])
        else:
            minHeap = insertToHeap(minHeap,arr[i])
        if minHeap[0] < maxHeap[0]:
            minHeap[0],maxHeap[0] = maxHeap[0],minHeap[0]
            heapify(minHeap,len(minHeap),0)
            heapify(maxHeap,len(minHeap),0)
    if len(maxHeap) == len(minHeap):
        return minHeap[0],maxHeap[0]
    else:
        return maxHeap[0]

arr = [2,7,1,5,9,18,1]
print(getMedian(arr))