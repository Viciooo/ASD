def mergeSort(arr,idx):
    if len(arr) > 1:
        mid = len(arr)//2
        L, R = arr[:mid], arr[mid:]
        mergeSort(L,idx)
        mergeSort(R,idx)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][idx] < R[j][idx]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr

arr = [1,2,3,4,5]
mergeSort(arr)
print(arr)
