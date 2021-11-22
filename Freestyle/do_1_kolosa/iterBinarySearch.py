def binSearch(arr,val):
    n = len(arr)
    low, high, mid = 0, n-1, (n-1)//2
    while low <= high:
        if val < arr[mid]:
            high = mid-1
            mid = (low+high)//2
        elif val > arr[mid]:
            low = mid+1
            mid = (low+high)//2
        else:
            return mid
    return -1

#complexity O(log(n))