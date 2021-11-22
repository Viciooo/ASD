def sumaPodzb(arr,T):
    n = len(arr)
    new = [[False]*(T+1) for _ in range(n+1)]
    for i in range(n+1):
        new[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, T + 1):
            if j<arr[i-1]:
                new[i][j] = new[i-1][j]
            if j>= arr[i-1]:
                new[i][j] = (new[i-1][j] or new[i-1][j-arr[i-1]])
    return new

arr = [2,6,4,3,9]
s = 23
n = len(arr)
print(sumaPodzb(arr,s))

