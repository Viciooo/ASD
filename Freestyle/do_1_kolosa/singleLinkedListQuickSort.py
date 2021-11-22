class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val) + "->" + str(self.next)

def tab_to_lista(tab):
    head = Node("!")
    last = head
    for i in tab:
        last.next = Node(i)
        last = last.next
    return head.next

def findEnd(first):
    p = first
    while p.next != None:
        p = p.next
    return p

def partition(low,high):
    pivot = high.val
    prev, p = low, low.next
    flag = True
    while p != high:
        if p.val > pivot:
            tmp = high.next
            q = Node(p.val)
            high.next = q
            q.next = tmp
            if flag == True:
                newHigh = q
                flag = False
            p, prev.next = p.next, p.next
        else:
            p, prev = p.next, p
    if flag:
        newHigh = high
    return high,prev,newHigh

def quickSort(low,high):
    if low != high and low.next != high:   
        i,j,k = partition(low,high)
        quickSort(low,j)
        quickSort(i,k)

arr = [5,1]
first = Node("!")
first.next = tab_to_lista(arr)
end = findEnd(first)
quickSort(first,end)
print(first)
        

