# zadanie2. W tym zadaniu nie można używać wbudowanego sortowania. Posiadając na
# wejściu przedziały w postaci [ai,bi] znajdź największy podprzedział gdzie 2 przedziały
# nachodzą na siebie. Zakładamy, że nie ma takiego punktu `j` w którym przecinają się więcej
# niż 2 przedziały.

#Główna idea:
#sortujemy przedziały po początkach w O(nlogn)
#przechodzimy liniowo sprawdzając każde dwa kolejne elementy i sprawdzamy dł nachodzenia spamiętujac najdłuższe przecięcie
#zł czasowa O(n^2) <- tu błąd w oszacowaniu zł
#pewnie rozwiązanie na 1 pkt bo da się w nlogn przedziałowym

def partition(arr, low, high,idx):
    i = (low-1)         # index of smaller element
    pivot = arr[high][idx]     # pivot
    for j in range(low, high):
        if arr[j][idx] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high,idx):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high,idx)
        quickSort(arr, low, pi-1,idx)
        quickSort(arr, pi+1, high,idx)

def intervals(T):
    #zakładam że nie napisano tego ale nie mogę zniszczyć tablicy więc robię kopię
    n = len(T)
    arr = [None for _ in range(n)]
    for i in range(n):
        arr[i] = T[i]

    quickSort(arr,0,n-1,1)
    quickSort(arr,0,n-1,0)

    _max, cut = 0, None
    for i in range(n-1):
        for k in range(i,-1,-1):
            if arr[k][1] < arr[i+1][0]:
                break
            if arr[k][0] < arr[i+1][0] and arr[k][1] > arr[i+1][1]:
                if _max < arr[i+1][1] - arr[i+1][0]:
                    _max = arr[i+1][1] - arr[i+1][0]
                    cut = (arr[i+1][0],arr[i+1][1])

            elif _max < arr[k][1]-arr[i+1][0]:
                _max = arr[k][1]-arr[i+1][0]
                cut = (arr[i+1][0],arr[k][1])
    return cut



T = [(1,5),(1,3),(4,6),(7,8),(8,10),(12,15)]
print(intervals(T),(1,3))
T = [(10,11),(9,10),(8,9),(1,2),(2,3),(6,7),(1,3),(11,15),(12,15)]
print(intervals(T),(12,15))
T = [(0,10),(1,3),(3,7),(7,11),(10,11)]
print(intervals(T),(3,7))