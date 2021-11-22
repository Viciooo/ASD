"""
No co, jaki algorytm jest każdy widzi.
Przechodzimy po macierzy adjencji, szukając pola z wodą. Następnie dla tego pola wywołujemy DFS, przechodząc po grafie
w poszukiwaniu kolejnych pól z wodą, idąc kolejno w prawo, dół, lewo i górę.
"""


def find_lakes(G):

    def DFSVisit(G, i, j, n):
        nonlocal visited, size
        visited[i][j] = True

        if j + 1 < n and G[i][j + 1] == 'W' and not visited[i][j + 1]:    # right
            size += 1
            DFSVisit(G, i, j + 1, n)

        if i + 1 < n and G[i + 1][j] == 'W' and not visited[i + 1][j]:    # down
            size += 1
            DFSVisit(G, i + 1, j, n)

        if j - 1 >= 0 and G[i][j - 1] == 'W' and not visited[i][j - 1]:     # left
            size += 1
            DFSVisit(G, i, j - 1, n)

        if i - 1 >= 0 and G[i - 1][j] == 'W' and not visited[i - 1][j]:    # up
            size += 1
            DFSVisit(G, i - 1, j, n)

    n = len(G)
    visited = [[False for _ in range(n)] for _ in range(n)]
    lakes = max_size = 0
    size = 1
    for i in range(n):
        for j in range(n):
            if G[i][j] == 'W' and not visited[i][j]:
                DFSVisit(G, i, j, n)
                max_size = max(max_size, size)
                size = 1
                lakes += 1

    return lakes, max_size


M = [['L', 'W', 'L', 'L', 'L', 'L', 'L', 'L'],
     ['L', 'W', 'L', 'W', 'W', 'L', 'L', 'L'],
     ['L', 'L', 'L', 'W', 'W', 'L', 'W', 'L'],
     ['L', 'W', 'W', 'W', 'W', 'L', 'W', 'L'],
     ['L', 'L', 'W', 'W', 'L', 'L', 'L', 'L'],
     ['L', 'W', 'L', 'L', 'L', 'L', 'W', 'W'],
     ['W', 'W', 'L', 'W', 'W', 'L', 'W', 'L'],
     ['L', 'L', 'L', 'W', 'L', 'L', 'L', 'L']]

print(find_lakes(M))