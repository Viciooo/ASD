def ale_sobie_sciezka_leci_hyhyhyhyhy(G):

    def DFSVisit(G, u, length=0):
        nonlocal visited, max_length,s
        if length > max_length:
            max_length = length

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v, length + 1)
            elif visited[v] and v == s:
                if length+1 > max_length:
                    max_length = length+1

    n = len(G)
    visited = [False for _ in range(n)]
    for u in range(n):
        if len(G[u]) > 2:
            visited[u] = True

    max_length = 0
    s = 0
    while s < n:
        if not visited[s]:
            DFSVisit(G, s)
        s += 1

    return max_length


G = [[1, 3], [0, 2, 4], [1], [0, 5], [1], [3, 6], [5]]
G1 = [[1, 6], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 0], []]
print(ale_sobie_sciezka_leci_hyhyhyhyhy(G))