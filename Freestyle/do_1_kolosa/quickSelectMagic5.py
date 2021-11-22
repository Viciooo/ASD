def swap(arr, a, b): 
	temp = arr[a] 
	arr[a] = arr[b] 
	arr[b] = temp 

def partition(arr, l, r, x): 
	for i in range(l, r): 
		if arr[i] == x: 
			swap(arr, r, i) 
			break
	x = arr[r] 
	i = l 
	for j in range(l, r): 
		if (arr[j] <= x): 
			swap(arr, i, j) 
			i += 1
	swap(arr, i, r) 
	return i

def insertionSort(arr): 
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >= 0 and key < arr[j] : 
      arr[j + 1] = arr[j] 
      j -= 1
    arr[j + 1] = key 
  return arr

def findMedian(arr, l, n): 
  t = [0]*n
  j = 0
  for i in range(l, l + n):
    t[j] = arr[i] 
    j+= 1
  insertionSort(t)
  return t[n//2] 

def kthSmallest(arr, l, r, k): 
  if (k >= 0 and k <= r - l + 1): 
    n = r - l + 1
    median = [] 
    i = 0
    while (i < n // 5): 
      median.append(findMedian(arr, l + i * 5, 5)) 
      i += 1
    if (i * 5 < n): 
      median.append(findMedian(arr, l + i * 5, n % 5)) 
      i += 1
    if i == 1: 
      medOfMed = median[0] 
    else: 
      medOfMed = kthSmallest(median, 0, i - 1, i // 2) 
    pos = partition(arr, l, r, medOfMed) 
    if (pos - l == k): 
      return arr[pos] 
    if (pos - l > k):
      return kthSmallest(arr, l, pos - 1, k) 
    return kthSmallest(arr, pos + 1, r, k - pos + l - 1) 

arr = [12, 3, 5, 7, 4, 19, 26] 
n = len(arr) 
k = 0
print("K'th smallest element is", 
kthSmallest(arr, 0, n - 1, k)) 