from queue import Queue

def getSolution(parent,s,u):
    if u == s:
        return [s]
    return getSolution(parent,s,parent[u]) + [u]

def bfsDjikstra(G,s,t):
    Q = Queue()
    n = len(G)
    d = [float("inf")  for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q.put((1,s,s,0))
    d[s] = 0
    while not Q.empty():
        w,u,last,edge = Q.get()
        w -= 1
        if w == 0:
            if visited[u]:
                continue
            visited[u] = True
            d[u] = d[last]+edge
            parent[u] = last
            for v,e in G[u]:
                if not visited[v]:
                    Q.put((e,v,u,e))
        elif w > 0:
            Q.put((w,u,last,edge))
    return d
#zł czasowa O(V+E)
#zł pamięciowa O(E) chyba
def bfsDjikstra(G,s,t):
    Q = Queue()
    n = len(G)
    d = [float("inf")  for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q.put((0,s,-1,0))
    d[s] = 0
    while not Q.empty():
        w,u,last,edge = Q.get()
        if w == 0:
            visited[u] = True
            if d[u] > d[last]+edge:
                d[u] = d[last]+edge
                parent[u] = last
            for v,e in G[u]:
                if not visited[v]:
                    Q.put((e,v,u,e))
        elif w > 0:
            Q.put((w-1,u,last,edge))
    return getSolution(parent,s,t)

#sprawdzić czy to ma sens

G = [[(1,1),(2,2)],[(4,4)],[(3,1)],[(4,1)],[]]
print(bfsDjikstra(G,0,4))
#poprawić


G1_matrix = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],
     [4, -1, 8, -1, -1, -1, -1, 11, -1],
     [-1, 8, -1, 7, -1, 4, -1, -1, 2],
     [-1, -1, 7, -1, 9, 14, -1, -1, -1],
     [-1, -1, -1, 9, -1, 10, -1, -1, -1],
     [-1, -1, 4, 14, 10, -1, 2, -1, -1],
     [-1, -1, -1, -1, -1, 2, -1, 1, 6],
     [8, 11, -1, -1, -1, -1, 1, -1, 7],
     [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

def fromMatrixToList(G):
    n = len(G)
    F = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                F[i].append([j,G[i][j]])
    return F

G1 = fromMatrixToList(G1_matrix)
print(bfsDjikstra(G1,0,8))