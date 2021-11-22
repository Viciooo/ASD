# Zadanie 3. (najdłuzszy podciag rosnacy) Prosze rozwiazac dwa nastepujace zadania:
# 1. Jak wykorzystac algorytm dla problemu najdłuzszego wspólnego podciagu do rozwiazania zadania
# najdłuzszego rosnacego podciagu?

#robimy drugią kopie tablicy arr nazwę ją arr1 - sortujemy ją rosnąco 
#odpalamy szukanie najdł wspólnego podciągu na arr i arr1
#odpowiedź to najdłuższy podciąg rosnący

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
        return arr

def longestCommSubsq(A,B):
    n = len(A)
    grid = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                grid[i][j] = 1 + grid[i-1][j-1]
            else:
                grid[i][j] = max(grid[i-1][j],grid[i][j-1])
    return grid[n][n]

# X = [2,3,5,1,7,3,4]
# n = len(X)
# W = [None]*n
# for i in range(n):
#     W[i] = X[i]
# Y = mergeSort(X)
# print(longestCommSubsq(W,Y))


# 2. Na wykładzie podalismy algorytm działajacy w czasie O(n^2). Prosze podac algorytm o złozonosci
# O(n log n).

def ceilIndex(arr, F, lght, val):
    start = 0
    end = lght
    while start <= end:
        mid = (start + end)//2
        if arr[F[mid]] < val and val <= arr[F[mid+1]]:
            return mid+1
        elif arr[F[mid]] < val:
            start = mid+1
        else:
            end = mid-1

def printSolution(R,i,arr):
    if i == -1:
        return
    else:
        printSolution(R,R[i],arr)
        print(arr[i],end=' ')

def nlognLis(arr):
    n = len(arr)
    T = [None]*n
    R = [-1]*n
    T[0] = 0
    l = 0
    for i in range(1,n):
        if arr[T[0]] > arr[i]:
            T[0] = i
        elif arr[T[l]] < arr[i]:
            l += 1
            T[l] = i
            R[T[l]] = T[l-1]
        else:
            index = ceilIndex(arr, T, l,arr[i])
            T[index] = i
            R[T[index]] = T[index-1]
    printSolution(R,T[l],arr)
    print()
    return l+1


arr = [3,4,-1,5,8,2,3,12,7,9,10]
print(nlognLis(arr))