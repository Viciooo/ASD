# Dana jest tablica z n liczbami całkowitymi. Zawiera ona bardzo dużo powtórzeń
# - co więcej, zaledwie O(log(n)) liczb jest unikatowe (reszta to powtórzenia).
# Napisz algorytm, który w czasie O(n*log(log(n))) posortuje taką tablicę.

import math

def weirdBinSearch(tmp,val):
    n = len(tmp)
    low, high, mid = 0, n-1, (n-1)//2
    while low <= high:
        if val < tmp[mid][1]:
            high = mid-1
            mid = (low+high)//2
        elif val > tmp[mid][1]:
            low = mid+1
            mid = (low+high)//2
        else:
            tmp[mid][0] += 1
            return 1
    return 0

def addVal(tmp,val):
    flag = weirdBinSearch(tmp,val)
    if flag == 0:
        i = 0
        while tmp[i][1] < val:
            i += 1
        t = tmp[i]
        for j in range(i+1,len(tmp)):
            t1 = tmp[j]
            tmp[j] = t
            t = t1
        tmp[i] = [1,val]

def ex6(arr):
    n = len(arr)
    tmp = [[0,float("inf")] for i in range(int(math.log(n,2)))]
    for i in arr:
        addVal(tmp,i)
    j = 0
    for i in range(n):
        if tmp[j][0] > 0:  
            arr[i] = tmp[j][1]
            tmp[j][0] -= 1
        else:
            j += 1
            arr[i] = tmp[j][1]
            tmp[j][0] -= 1

arr = [1,1,1,8,8,8,1,4]
ex6(arr)
print(arr)
