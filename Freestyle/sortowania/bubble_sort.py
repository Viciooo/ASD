def bubbleSort_v1(arr):
    n = len(arr)
    notSorted = True
    while notSorted:
        notSorted = False
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                notSorted = True
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

def bubbleSort_v2(arr): 
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n): 
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5,1,4,2,8]
bubbleSort_v2(arr)
print(arr)