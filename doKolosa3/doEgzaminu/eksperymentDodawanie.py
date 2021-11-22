def solve(arr):
    n = len(arr)
    S = [[0 for _ in range(n)] for _ in range(n)]
    F = [[float("inf") for _ in range(n)] for _ in range(n)]
    S[0][0] = arr[0]
    F[0][0] = abs(arr[0])
    for i in range(1,n):
        S[0][i] = arr[i] + S[0][i-1]
        F[i][i] = abs(arr[i])
        F[i-1][i] = abs(arr[i]+arr[i-1])

    for i in range(n):
        for j in range(i,n):
            S[i][j] = S[0][j] - S[0][i] + arr[i]
    
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            for k in range(i,j):
                F[i][j] = min(F[i][j],max(F[i][k],F[k+1][j],abs(S[i][j])))
    return F[0][n-1]

arr1 = [1,-5,2]
print(solve(arr1))
arr2 = [-3,2,7,1,8,-16]
print(solve(arr2))
arr3 = [1,2,3,4,-5]
print(solve(arr3))

t = [1, -5, 3, -1, -3, 5, -8, 3, 2, -7, 6, 3]
print(solve(t))

#zł czasowa O(n^3)
#zł pamięciowa O(n^2)