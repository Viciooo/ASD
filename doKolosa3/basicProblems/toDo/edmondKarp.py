from queue import Queue

def changeGraph(G,parent,bt,s,t):
    if t == s:
        return []
    G[parent[t]][t] -= bt
    G[t][parent[t]] += bt
    return changeGraph(G,parent,bt,s,parent[t]) + [(s,t)]

def matrixBfs(G,s,t):
    q = Queue()
    n = len(G)
    visited = [False]*n
    parent = [None for _ in range(n)]
    q.put((s,float("inf")))
    visited[s] = True
    while not q.empty():
        u,bt = q.get()
        if u == t:
            return bt,changeGraph(G,parent,bt,s,t)
        for v in range(n):
            if G[u][v] != 0:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    bt = min(bt,G[u][v])
                    q.put((v,bt))
    return float("inf"),None

def edmondKarp(G,s,t):
    maxFlow = 0
    paths = []
    flow,p = matrixBfs(G,s,t)
    while flow != float("inf"):
        maxFlow += flow
        paths.append([p,flow])
        flow,p = matrixBfs(G,s,t)
    for i in paths:
        print(i)
    return maxFlow

G1 = [[0, 3, 4, 0, 0, 0],
     [0, 0, 0, 2, 2, 0],
     [0, 2, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 5],
     [0, 0, 0, 0, 0, 0]]
s1 = 0
t1 = 5
odp1 = 6
print(edmondKarp(G1,s1,t1))

G2 = [[0, 0, 0, 0, 2, 0, 7],
     [0, 0, 0, 2, 3, 0, 0],
     [2, 0, 0, 0, 0, 3, 0],
     [0, 0, 0, 0, 4, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 0, 0],
     [0, 4, 5, 0, 0, 0, 0]]

s2 = 0
t2 = 4
odp2 = 8
print(edmondKarp(G2,s2,t2))
