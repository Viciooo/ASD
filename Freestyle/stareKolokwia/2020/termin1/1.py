import math

class node:
    def __init__(self,val,next=None):
        self.next = next
        self.val = val

def pop(v,curr,prev):
    first = prev
    flag = True #liczba jednokrotna
    while curr != None:
        if curr.val == v:
            flag = False
            prev.next, curr = curr.next, curr.next
        else:
            curr, prev = curr.next, curr
    return flag,first

def count(v,maxi):
    j = w = 0
    first = node("!")
    q = first
    while v != 0:
        q.next = node(v%10)
        v //= 10
        q = q.next

    prev, p = first.next, first.next.next
    while p != None:
        a = pop(prev.val,p,prev)
        if a[0] == True:
            j+=1
        else:
            w+=1
        if a[1] == None or a[1].next == None:
            return (j + w*10**(-maxi//2))
        else:
            prev, p = a[1].next, a[1].next.next
    j += 1
    return (j + w*10**(-maxi//2))
    
def partition(arr, arr1, low, high): 
    i = (low-1)         
    pivot = arr[high]    

    for j in range(low, high): 
        if arr[j] >= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            arr1[i], arr1[j] = arr1[j], arr1[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    arr1[i+1], arr1[high] = arr1[high], arr1[i+1]
    return (i+1) 

def quickSort(arr, arr1, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
        pi = partition(arr, arr1, low, high) 
        quickSort(arr, arr1, low, pi-1) 
        quickSort(arr, arr1, pi+1, high) 


def main(arr):
    n = len(arr)
    new = [None]*n
    maxi = int(math.log10(max(arr)))+1
    for i in range(n):
        new[i] = count(arr[i],maxi)
    quickSort(new,arr,0,n-1)
    return arr

arr = [455,123,1266,114577]
print(main(arr))

#ale to jest okropne rozwiązanie ;-; złożoność O(n^2) chyba
