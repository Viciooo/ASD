def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

arr = [5,1,4,2,8]
print(selectionSort(arr))