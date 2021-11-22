from queue import PriorityQueue

def remove_vertices(G, k):
    n = len(G)
    Q = PriorityQueue()
    degree = [0 for _ in range(n)]
    for v in range(n):
        degree[v] = len(G[v])
        Q.put([degree[v], v])

    while not Q.empty():
        d, u = Q.get()
        if d >= k:
            break

        if degree[u] > 0:
            for v in G[u]:
                degree[v] -= 1
                Q.put([degree[v], v])

            degree[u] = 0

    res = []
    for v in range(n):
        if degree[v] > 0:
            res.append(v)

    return res


G = [
    [1],
    [0, 2, 3],
    [1, 3, 5],
    [1, 2, 5, 4],
    [3, 5],
    [2, 4, 6],
    [7, 5],
    [6]
]
print(remove_vertices(G, 2))