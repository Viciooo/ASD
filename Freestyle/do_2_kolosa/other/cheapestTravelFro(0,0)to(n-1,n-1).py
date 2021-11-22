def findLowestPrice(M):
    m = len(M)
    n = len(M[0])
    F = [[0 for _ in range(n)] for _ in range(m)]
    F[0][0] = M[0][0]
    for i in range(1,max(n,m)):
        if i < n:
            F[0][i] = M[0][i] + F[0][i-1]
        if i < m:
            F[i][0] = M[i][0] + F[i-1][0]
    for i in range(1,m):
        for j in range(1,n):
            F[i][j] = min(F[i-1][j],F[i][j-1]) + M[i][j]
    for i in F:
        print(i)
    getPath(M,F,m-1,n-1)
    print((m-1,n-1))
    return 

def getPath(M,F,i,j):
    if i == j == 0:
        return
    if i > 0 and F[i][j]-M[i][j] == F[i-1][j]:
        getPath(M,F,i-1,j)
        print((i-1,j),end=' , ')
    else:
        getPath(M,F,i,j-1)
        print((i,j-1),end=' , ')

M = [[0,2,4,3],
     [3,15,3,2],
     [11,6,2,9]]
findLowestPrice(M)
