from zad1testy import runtests

def floydWarshall(G):
    #G to macierz
    n = len(G)
    D = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = 0
            if G[i][j] != 0:
                D[i][j] = G[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D

from queue import Queue



def get_solution(G, parent, x, y, a, b):
    if a == x and b == y:
        return [(a, b)]

    return get_solution(G, parent, x, y, parent[a][b][0], parent[a][b][1]) + [(a, b)]


def BFS(G, x, y):
    n = len(G)
    Q = Queue()
    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[[None, None] for _ in range(n)] for _ in range(n)]
    parent[x][y] = [x, y]
    Q.put([x, y])
    visited[x][y] = True
    while not Q.empty():
        a, b = Q.get()
        for i in range(n):
            for j in range(n):
                if G[a][b][i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    parent[i][j] = [a, b]
                    Q.put([i, j])

    return get_solution(G, parent, x, y, y, x)


def keep_distance(M, x, y, d):
    n = len(M)
    S = floydWarshall(M)
    G = [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for a in range(n):
                for b in range(n):
                    if (i != b or j != a) and d <= S[a][b] < float("inf") and (M[i][a] > 0 or i == a) and\
                            (M[j][b] > 0 or j == b):
                        G[i][j][a][b] = 1

    return BFS(G, x, y)


runtests( keep_distance )