from queue import Queue


def build_graph(digits):
    n = len(digits)
    G = [[] for _ in range(1000)]   #TODO
    for i in range(1000):
        for j in range(n):
            G[i].append((i + digits[j]) % 1000)

    return G


def safe(digits, target, display):
    # G = (V, E), s należy do V; w naszym przypadku G to lista sąsiedztwa
    G = build_graph(digits)
    n = len(G)
    Q = Queue()
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]

    visited[display] = True
    d[display] = 0
    Q.put(display)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                if v == target:
                    return d[v]

                visited[v] = True
                parent[v] = u
                Q.put(v)

    return


target = 100
display1 = 50   # [30, 20]
display2 = 900     # [35, 35, 35, 35, 20, 5]
display3 = 51   # None
digits = [5, 10, 20, 30, 35]

print(safe(digits, target, display1))
print(safe(digits, target, display2))
print(safe(digits, target, display3))