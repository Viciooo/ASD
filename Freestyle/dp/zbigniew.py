def zbigniew( A ):
    n = len(A)
    m = sum(A)
    m = max(n, m - n)
    F = [[float("inf") for _ in range(m)] for _ in range(n)]
    F[0][A[0]] = 0

    for i in range(1, n):
        for j in range(m):
            for k in range(i):
                if m-(i-k) > j-A[i] >= 0:
                    F[i][j] = min(F[i][j], F[k][j + (i - k) - A[i]] + 1)

    def getSolution(i,j,k):
        nonlocal m,F,A
        if i == 0:
            return []
        if m-(i-k) > j-A[i] >= 0 and F[i][j] == F[k][j+(i-k)-A[i]]+1:
            return getSolution(k,j+(i-k)-A[i],n-1)+[k]
        else:
            return getSolution(i,j,k-1)

    _min, resJ = float("inf"), None
    for j in range(A[n-1],m):
        if F[n-1][j] < _min:
            _min = F[n-1][j]
            resJ = j
    return getSolution(n-1,resJ,n-1)





A = [2, 2, 1, 0, 0, 0]
B = [4, 5, 2, 4, 1, 2, 1, 0]
print(zbigniew(A))
print(zbigniew(B))
C = [6, 0, 2, 0, 3, 0, 1, 0, 1, 0, 0, 1]
D = [2, 0, 15, 0, 3, 0, 0, 0, 8, 0, 0, 0]
print(zbigniew(D))
# [0, 1, 2]
# [0, 3]
# [0, 2]
