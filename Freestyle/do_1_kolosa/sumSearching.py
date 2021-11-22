# Dana jest posortowana tablica A[1...n] oraz liczba x. Prosze napisac program,
# który stwierdza czy istnieja indeksy i oraz j takie, ze A[i] + A[j] = x.

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L, R = arr[:mid], arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
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

def search(A,x):
    mergeSort(A)
    n = len(A)
    low, high = 0, n-1
    s = A[low]+A[high]
    print(A)
    while low < high and s != x:
        if s < x:
            low += 1
        else:
            high -= 1
        s = A[low]+A[high]
    if s == x:
        return (A[low],A[high])
    else: return -1

arr = [2,5,1,7,-3,2,0,-14]
print(search(arr,-13))