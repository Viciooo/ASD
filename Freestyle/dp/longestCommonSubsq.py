# Zadanie 2. (najdłuzszy wspólny podciag) Mamy dane dwie tablice, A[n] i B[n]. Nalezy znalezc długosc
# ich najdłuzszego wspólnego podciagu. (Klasyczny algorytm dynamiczny O(n^2)).

def longestCommSubsq(A,B):
    n = len(A)
    grid = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                grid[i][j] = 1 + grid[i-1][j-1]
            else:
                grid[i][j] = max(grid[i-1][j],grid[i][j-1])
    return grid[n][n]

X = "AGGTABS"
Y = "GXTXAYB"
print(longestCommSubsq(X,Y))

#space usage can be optimalized to O(2n) instead of O(n^2)