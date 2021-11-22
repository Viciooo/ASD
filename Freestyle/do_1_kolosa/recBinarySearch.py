def binSearch(arr,val,low,high):
    mid = (low+high)//2
    if low <= high:
        if val < arr[mid]:
            return binSearch(arr,val,low,mid-1)
        elif val > arr[mid]:
            return binSearch(arr,val,mid+1,high)
        elif val == arr[mid]:
            return mid
    return -1

