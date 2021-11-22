def klocki(arr):
    n = len(arr)
    F = [0 for _ in range(n)]
    F[0] = 1
    for i in range(1,n):
        a = arr[i][0]
        b = arr[i][1]
        for j in range(i):
            c = arr[j][0]
            d = arr[j][1]
            if (c <= a and a < d) or (c > a and c < b):
                F[i] = max(F[i],F[j]+1)
    return max(F)

arr = [(1,3),(2,5),(0,3),(8,9),(4,6),(0,2)]
print(klocki(arr))