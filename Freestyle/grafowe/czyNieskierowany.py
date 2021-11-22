def check_if_undirected(G):
    def DFSVisit(G, u, start):
        flag = False
        nonlocal visited, parent, res
        visited[u] = True
        for v in G[u]:
            if v == parent[u]:
                flag = True

            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v, start)

        if not flag and u != start:
            res = False

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    res = True
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u, u)
            if not res:
                return False

    return True


G_directed = [[1], [2], [3], []]
G_undirected = [[1, 3], [2, 0], [3, 1], [0, 2]]
print(check_if_undirected(G_directed))
print(check_if_undirected(G_undirected))