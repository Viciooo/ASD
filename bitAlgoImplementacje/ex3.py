# Mamy daną tablicę A z n liczbami naturalnymi. 
# Proszę zaproponować algorytm o złożoności O(n), 
# który stwierdza, czy w tablicy ponad połowa elementów ma jednakową wartość.

def ex3(arr):
    lider = arr[0]
    cnt = 1
    for i in range(1,len(arr)):
        if arr[i] == lider:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            lider = arr[i]
            cnt += 1
    if cnt > 0:
        cnt = 0
        for i in range(len(arr)):
            if arr[i] == lider:
                cnt += 1
    return lider if cnt >= len(arr)//2 + 1 else -1 

arr = [1,2,1,1,3,2,2,2,2]
print(ex3(arr))