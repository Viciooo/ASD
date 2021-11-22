def transitiveClosure(G):
    n = len(G)
    T = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                T[i][j] = 1
            else:
                T[i][j] = G[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] or (T[i][k] and T[k][j])
    return T

G = [[0,0,0,0],
     [0,0,1,1],
     [0,1,0,0],
     [1,0,1,0]]

print(transitiveClosure(G))