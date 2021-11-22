#Robię linkedlisty z tych tablic co dostajemy potem robię z nich kopiec min i dolepiam do wyniku następujące korzenie
#proste ale uciążliwe implementacyjnie
#zł obliczeniowa O(nlogk) n razy wywołujemy heapify którego czas to logn
#zł pamięciowa O(n)

class Node:
    def __init__(self,val):
        self.next = None
        self.val = val

def heapify(arr,n,i):
    root = i
    l = 2*i + 1
    r = 2*i + 2
    if arr[root] == None:
        if l < n and arr[l] == None:
            if r < n and arr[r] == None:
                return
            root = r
        elif r < n and arr[r] == None:
            root = l
        else:
            if l < n:
                root = l
            elif r < n:
                root = r
                
    if r < n and arr[r] != None and arr[root].val > arr[r].val:
        root = r
    if r < n and arr[l] != None and arr[root].val > arr[l].val:
        root = l
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr,n,root)

def buildHeap(arr, n): 
    startIdx = n // 2 - 1 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i) 

def makeList(arr):
    start = Node("!")
    p = start
    for i in arr:
        p.next = Node(i)
        p = p.next
    return start.next

def mergeLists(arr):
    heap = []
    n = len(arr)
    solution = []
    for i in arr:
        heap.append(makeList(i))
    buildHeap(heap,n)
    while True:
        solution.append(heap[0].val)
        heap[0] = heap[0].next
        heapify(heap,n,0)
        if heap[0] == None:
            return solution

arr = [[5,15,25],[0,10,20],[0,1,2,4,5]]
print(mergeLists(arr))