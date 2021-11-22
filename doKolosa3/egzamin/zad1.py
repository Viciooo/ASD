#Piotr Witek
#Opis algorytmu:
#Korzystam ze stabilności mergeSort'a i sortuję tablice [wartość na i'tym idx w T,i] po 0 miejscu
#k będzie max różnicą pomiędzy indexem w posortowanej a indexem podanym na pozycji 1 

#zł obliczeniowa O(nlogn) narzucona przez sortowanie
#zł pamięciowa O(n) pomimo trzochę nieładnych sliców które jednak nie wpływają na złożoność


from zad1testy import runtests


def mergeSort(arr,idx):
    if len(arr) > 1:
        mid = len(arr)//2
        left, right = arr[:mid], arr[mid:]
        mergeSort(left,idx)
        mergeSort(right,idx)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][idx] <= right[j][idx]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
        return arr

def chaos_index( T ):
    n = len(T)
    arr = [None for _ in range(n)]
    for i in range(n):
        arr[i] = [T[i],i]
    mergeSort(arr,0)
    k = 0
    for i in range(n):
        k = max(k,abs(arr[i][1]-i))
    return k


runtests( chaos_index )
