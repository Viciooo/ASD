def find(arr):
    n = len(arr)
    s = 0
    new = [0 for _ in range(n)]
    for i in range(n):
        new[i] += s
        s += arr[i]
    s = 0
    for i in range(n-1,-1,-1):
        new[i] -= s
        s += arr[i]
    for i in range(n):
        if new[i] == 0:
            print(i)

def betterFind(arr):
    n = len(arr)
    sumOfAll = 0
    for i in arr:
        sumOfAll += i
    s = 0
    for i in range(n):
        if s == sumOfAll-s-arr[i]:
            print(i)
        s += arr[i]

arr = [0, -3, 5, -4, -2, 3, 1, 0]
betterFind(arr)