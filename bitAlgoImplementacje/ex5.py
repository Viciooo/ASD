# Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k].
# Zamieniono 10 liczb z tej tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne).
# Napisz algorytm, który posortuje tablicę w czasie O(n).

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
    return arr

def countingSort(arr,k):
    k += 1
    count = [0]*k
    n = len(arr)
    for i in range(n):
        count[arr[i]] += 1
    for i in range(1,k):
        count[i] += count[i-1]
    new = [None]*n
    for i in range(n-1,-1,-1):
        count[arr[i]] -= 1
        new[count[arr[i]]] = arr[i]
    return new

def getTheDataReady(arr,k):
    m = len(arr)
    normal = [0 for _ in range(m-10)]
    weird = [0 for _ in range(10)]
    w = n = 0
    for i in arr:
        if i < 0 or i > k:
            weird[w] = i
            w += 1
        else:
            normal[n] = i
            n += 1
    weird = insertionSort(weird)
    normal = countingSort(normal,k)
    w = n = 0
    for i in range(m):
        if w < 10 and n < m-10:
            if weird[w] < normal[n]:
                arr[i] = weird[w]
                w += 1
            else:
                arr[i] = normal[n]
                n += 1
        elif w == 10:
            for j in range(i,m):
                arr[j] = normal[n]
                n += 1
            break
        else:
            for j in range(i,m):
                arr[j] = weird[w]
                w += 1
            break

arr = [-1,2,3,4,1,15,14,12,-15,-7,-2,0,22,21,911]
getTheDataReady(arr,5)
print(arr)