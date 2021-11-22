def find_path(G):

    def DFSVisit(G, n, i=0, j=0, dist=0):
        nonlocal min_dist, visited
        if i == n - 1 and j == n - 1:
            min_dist = min(min_dist, dist)
            return

        visited[i][j] = True
        if j + 1 < n and G[i][j + 1] == 'L' and not visited[i][j + 1]:    # right
            DFSVisit(G, n, i, j + 1, dist + 1)
            visited[i][j + 1] = False

        if i + 1 < n and G[i + 1][j] == 'L' and not visited[i + 1][j]:    # down
            DFSVisit(G, n, i + 1, j, dist + 1)
            visited[i + 1][j] = False

        if j - 1 >= 0 and G[i][j - 1] == 'L' and not visited[i][j - 1]:     # left
            DFSVisit(G, n, i, j - 1, dist + 1)
            visited[i][j - 1] = False

        if i - 1 >= 0 and G[i - 1][j] == 'L' and not visited[i - 1][j]:    # up
            DFSVisit(G, n, i - 1, j, dist + 1)
            visited[i - 1][j] = False

    n = len(G)
    visited = [[False for _ in range(n)] for _ in range(n)]
    min_dist = float("inf")
    DFSVisit(G, n)

    return min_dist + 1


M = [['L', 'W', 'L', 'L', 'L', 'L', 'L', 'L'],
     ['L', 'W', 'L', 'W', 'W', 'L', 'L', 'L'],
     ['L', 'L', 'L', 'W', 'W', 'L', 'W', 'L'],
     ['L', 'W', 'W', 'W', 'W', 'L', 'W', 'L'],
     ['L', 'L', 'W', 'W', 'L', 'L', 'L', 'L'],
     ['L', 'W', 'L', 'L', 'L', 'L', 'W', 'W'],
     ['W', 'W', 'L', 'W', 'W', 'L', 'W', 'L'],
     ['L', 'L', 'L', 'W', 'L', 'L', 'L', 'L']]

print(find_path(M))