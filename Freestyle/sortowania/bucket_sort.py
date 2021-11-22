def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

def bucketSort(arr):
    n = len(arr)
    norm = max(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        norm_num = num / norm
        bucketIdx = int(n * norm_num)
        buckets[bucketIdx].append(num)
    for i in range(n):
        insertionSort(buckets[i])
    output = []
    for i in range(n):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
    return output

arr = [7,1,2,18,9,15,3]
arr = bucketSort(arr)
print(arr)

