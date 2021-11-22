# Zadanie 4. (Pojemniki z woda) Mamy serie pojemników z woda, połaczonych (kazdy z kazdym) rurami.
# Pojemniki maja kształty prostokatów, rury nie maja objetosci (powierzchni). Kazdy pojemnik opisany jest
# przez współrzedne lewego górnego rogu i prawego dolnego rogu.
# Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiscie woda rurami spłyneła do najnizszych
# pojemników). Prosze zaproponowac algorytm Obliczajacy ile pojemników zostało w pełni zalanych.

def modifyData(tpl):
    yCeil, yBottom = tpl[1], tpl[3]
    width = abs(tpl[0] - tpl[2])
    bottom = (yBottom,width,"bottom")
    ceil = (yCeil,width,"ceil")
    return bottom,ceil

def mergeSortTpl(arr:list):
    if len(arr) > 1:
        mid = len(arr)//2
        L, R = arr[:mid], arr[mid:]
        mergeSortTpl(L)
        mergeSortTpl(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
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

def insertWater(arr,A):
    cnt = lastHeight = currWidth = 0
    for i in range(len(arr)):
        A -= (arr[i][0]-lastHeight)*currWidth
        if A < 0:
            break
        if arr[i][2] == "bottom":
            currWidth += arr[i][1]
        else:
            currWidth -= arr[i][1]
            cnt += 1
        lastHeight = arr[i][0]
    return cnt

def main(arr,A):
    n = len(arr)
    new = [None]*2*n
    j = 0
    for i in arr:
        new[j], new[j+1] = modifyData(i)
        j += 2
    new = mergeSortTpl(new)
    return insertWater(new,A)

    


arr = [(-4,-2,-2,-5),(-1,-3,1,-4),(1,1,3,-2),(5,-1,8,-3)]
print(main(arr,19))
