from queue import PriorityQueue

def getSolution(parent,s,u):
    if u == s:
        return [s]
    return getSolution(parent,s,parent[u]) + [u]

def min_weight_vertex(visited, d, n):
    mini, mini_index = float("inf"), -1
    for i in range(n):
        if not visited[i] and d[i] < mini:
            mini = d[i]
            mini_index = i

    return mini_index


def dijkstra_matrix(G, s, t):
    n = len(G)
    d = [float("inf") for _ in range(n)]
    d[s] = 0
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    for _ in range(n):
        min_vertex = min_weight_vertex(visited, d, n)
        visited[min_vertex] = True
        for j in range(n):
            if G[min_vertex][j] != -1 and not visited[j] and d[j] > d[min_vertex] + G[min_vertex][j]:
                d[j] = d[min_vertex] + G[min_vertex][j]
                parent[j] = min_vertex
    return getSolution(parent,s,t)


G = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
     [4, -1, 8, -1, -1, -1, -1, 11, -1],
     [-1, 8, -1, 7, -1, 4, -1, -1, 2],
     [-1, -1, 7, -1, 9, 14, -1, -1, -1],
     [-1, -1, -1, 9, -1, 10, -1, -1, -1],
     [-1, -1, 4, 14, 10, -1, 2, -1, -1],
     [-1, -1, -1, -1, -1, 2, -1, 1, 6],
     [8, 11, -1, -1, -1, -1, 1, -1, 7],
     [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

print(dijkstra_matrix(G, 0,8))


from queue import PriorityQueue

def dijkstra(G,s):
    Q = PriorityQueue()
    n = len(G)
    parent = [-1 for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 0
    Q.put((0,s))
    while not Q.empty():
        u = Q.get()[1]
        if not visited[u]:
            visited[u] = True
            for v,w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    parent[v] = u
                Q.put((d[v],v))
    return d

# G = [[(1,1),(2,2)],[(4,4)],[(3,1)],[(4,1)],[]]
# print(dijkstra(G,0))