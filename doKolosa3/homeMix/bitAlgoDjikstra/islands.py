from queue import PriorityQueue


def cost_index(w):
    if w == 1:
        return 0
    if w == 5:
        return 1
    if w == 8:
        return 2

def build_graph(G):
    n = len(G)
    H = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                H[u].append([v, G[u][v]])
    return H


def islands(G, A, B):
    n = len(G)
    Q = PriorityQueue()
    G = build_graph(G)
    d = [[float("inf") for _ in range(3)] for _ in range(n)]
    visited = [[False for _ in range(3)] for _ in range(n)]

    for u in range(3):
        d[A][u] = 0
        Q.put([0, A, u])

    while not Q.empty():
        cost, u, t = Q.get()
        if not visited[u][t]:
            visited[u][t] = True
            for v, w in G[u]:
                if w != cost_index(t) and d[v][cost_index(w)] > d[u][t] + w:
                    d[v][cost_index(w)] = d[u][t] + w
                    Q.put([d[v][cost_index(w)], v, cost_index(w)])

    return min(d[B])


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]

print(islands(G1, 5, 2))