def countingSort(arr,k):
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

arr = [5,2,3,9,8,1,0]
print(countingSort(arr,10))