# Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k, 
# które są w nim równomiernie rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze 
# jest proporcjonalne do pola tego obszaru.Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości 
# do punktu (0, 0), tzn. d = sqrt(x2 + y2).

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
        

def ex1(arr,k):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        norm_num = (num[0]**2 +num[1]**2) / (k*k)
        bucketIdx = int(n * norm_num - 0.001)
        buckets[bucketIdx].append(num)
    for i in range(n):
        insertionSort(buckets[i])
    output = []
    for i in range(n):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
    return output
