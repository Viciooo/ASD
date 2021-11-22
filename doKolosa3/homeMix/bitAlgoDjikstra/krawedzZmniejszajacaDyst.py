from queue import PriorityQueue


def dijkstra(G, s):
    # G = (V, E), s należy do V; w naszym przypadku G to lista sąsiedztwa
    n = len(G)
    Q = PriorityQueue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]

    d[s] = 0
    Q.put([0, s])
    while not Q.empty():
        _, u = Q.get()
        if not visited[u]:
            for v, w in G[u]:
                if not visited[v]:
                    if d[v] > d[u] + w:
                        parent[v] = u
                        d[v] = d[u] + w

                    Q.put([d[v], v])

        visited[u] = True

    return d


def implant_5g_chip(G, E, s, t):
    n = len(G)
    d_s = dijkstra(G, s)
    d_t = dijkstra(G, t)
    opt_val = float("inf")
    res_edge = -1
    for u, v, w in E:
        diff = d_s[t] - (d_s[u] + w + d_t[v])
        if d_s[t] > d_s[u] + w + d_t[v] and opt_val > diff:
            opt_val = diff
            res_edge = (u, v, w)

    return res_edge


G = [
    [[1, 10], [3, 5]],
    [[0, 10], [2, 10]],
    [[1, 10], [3, 2]],
    [[0, 5], [2, 2]]
]

E = [[0, 2, 2], [0, 3, 6], [3, 1, 3]]  # treating as undirected

print(implant_5g_chip(G, E, 0, 3))