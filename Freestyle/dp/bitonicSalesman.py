def d(a,b):
    return ((a[1]-b[1])**2 + (a[2]-b[2])**2)**(0.5)

def salesman(C):
    C = sorted(C,key=lambda idx: idx[1])
    n = len(C)
    D = [[None]*n for _ in range(n)]
    for i in range(n*n):
        if i//n < i%n:
            D[i//n][i%n] = d(C[i//n],C[i%n])
    F = [[float("inf")]*n for _ in range(n)]
    F[0][1] = D[0][1]
    for k in range(n*n):
        i = k//n
        j = k%n
        if i < j:
            F[i][j] = tspf(i,j,F,D)
    solution = float("inf")
    for i in range(n-2):
        if F[i][n-1]+D[i][n-1] < solution:
            solution = F[i][n-1]+D[i][n-1]
    return solution

def tspf(i,j,F,D):
    if F[i][j] < float("inf"):
        return F[i][j]
    if i == j-1:
        best = float("inf")
        for k in range(j-1):
            best = min(best,tspf(k,j-1,F,D)+D[k][j])
        F[j-1][j] = best
    else:
        F[i][j] = tspf(i,j-1,F,D)+D[j-1][j]
    return F[i][j]





C = [["Wrocław", 0, 2], ["Warszawa",4,3],
["Gdansk", 2,4], ["Kraków",3,1]]
print(salesman(C))
# print(C)
# print(d(C[0],C[2])+d(C[2],C[1]))
# print(d(C[0],C[1]))