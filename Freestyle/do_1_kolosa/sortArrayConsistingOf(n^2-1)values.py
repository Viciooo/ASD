def convertData(arr):
    n = len(arr)
    new = [None]*n
    for i in range(n):
        a = arr[i] // n
        b = arr[i] % n
        new[i] = (a,b)
    return new

def sortIt(arr,idx):
    n = len(arr)
    c = [0]*n
    new = [None]*n
    for j in range(n):
        c[arr[j][idx]] += 1
    for j in range(1,n):
        c[j] += c[j-1]
    for j in range(n-1,-1,-1):
        c[arr[j][idx]] -= 1
        new[c[arr[j][idx]]] = arr[j]
    return new

def getListSorted(arr):
    n = len(arr)
    new = convertData(arr)
    new = sortIt(new,1)
    new = sortIt(new,0)
    for i in range(n):
        arr[i] = new[i][0]*n+new[i][1]

arr = [5,2,13,17,12]
getListSorted(arr)
print(arr)