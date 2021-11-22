def getSolution(P,i,j):
    if j == i:
        return []
    return getSolution(P,i,P[i][j]) + [j]

def floydWarshall(G):
    #G to macierz
    n = len(G)
    D = [[None for _ in range(n)] for _ in range(n)]
    P = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            D[i][j] = G[i][j]
            if G[i][j] != float("inf") and i != j:
                P[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = P[k][j]#tu
    return D

G = [[0,3,float("inf"),7],
    [8,0,2,float("inf")],
    [5,float("inf"),0,1],
    [2,float("inf"),float("inf"),0]]

# [0, 3, 5, 6]      
# [5, 0, 2, 3]      
# [3, 6, 0, 1]      D
# [2, 5, 7, 0]

# [[0, 0, 1, 2],
# [3, 0, 1, 2],
# [3, 0, 0, 2],     P
# [3, 0, 1, 0]]

# [[], [1], [1, 2], [1, 2, 3]]
# [[2, 3, 0], [], [2], [2, 3]]
# [[3, 0], [3, 0, 1], [], [3]]  solution
# [[0], [0, 1], [0, 1, 2], []]
print(floydWarshall(G))