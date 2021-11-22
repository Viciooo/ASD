# Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. 
# Napisz algorytm, który posortuje tę tablicę w czasie O(n).
# Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.

def insertionSortByOrd(arr,start,idx): 
    for i in range(start+1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= start and ord(key[idx]) < ord(arr[j][idx]) : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

def ex2(arr,n):
    m = len(arr)
    new = [0]*m
    lgth = (n//2)
    c = [0]*lgth
    l = [0]*lgth
    for i in arr:
        c[len(i)] += 1
        l[len(i)] += 1
    for i in range(1,lgth):
        c[i] += c[i-1]
    for i in range(m-1,-1,-1):
        c[len(arr[i])] -= 1
        new[c[len(arr[i])]] = arr[i]
    start = m
    for i in range(lgth-1,0,-1):
        start -= l[i]
        if l[i] == 1 and i == lgth-1:
            continue
        insertionSortByOrd(new,start,i-1)
    return new


T1= ["wrt","wrf","er","ett","rftt"]
arr = ex2(T1,15)
print(T1)

