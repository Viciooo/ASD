from queue import PriorityQueue
def prep(G,P):
    n = len(G)
    L = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                L[i].append([j,G[i][j]])
    betterP = [False for _ in range(n)]
    for i in P:
        betterP[i] = True
    return L,betterP

def getSolution(parent,a,i,f):
    if i == a:
        return [a]
    return getSolution(parent,a,parent[i][f][0],parent[i][f][1])+[i]

def jak_dojade(G,P,d,a,b):
    n = len(G)
    G,P = prep(G,P)
    q = PriorityQueue()
    parent = [[None for _ in range(d+1)] for _ in range(n)]
    dist = [[float("inf") for _ in range(d+1)] for _ in range(n)]
    visited = [[False for _ in range(d+1)] for _ in range(n)]
    for i in range(d+1):
        dist[a][i] = 0
    q.put((0,a,d))
    while not q.empty():
        _,u,f = q.get()
        if not visited[u][f]:
            visited[u][f] = True
            for v,cost in G[u]:
                if cost <= f:
                    if dist[v][f-cost] > dist[u][f] + cost and not P[v]:
                        parent[v][f-cost] = (u,f)
                        dist[v][f-cost] = dist[u][f] + cost
                        q.put((dist[v][f-cost],v,f-cost))
                    elif dist[v][d] > dist[u][f] + cost and P[v]:
                        parent[v][d] = (u,f)
                        dist[v][d] = dist[u][f] + cost
                        q.put((dist[v][d],v,d))

    _min, fuel = float("inf"),None
    for i in range(d+1):
        if dist[b][i] < _min:
            fuel = i
            _min = dist[b][i] 

    return getSolution(parent,a,b,fuel) if fuel != None else None

#O(d*Elog(Vd))

G = [[-1, 6,-1, 5, 2],
    [-1,-1, 1, 2,-1],
    [-1,-1,-1,-1,-1],
    [-1,-1, 4,-1,-1],
    [-1,-1, 8,-1,-1]]
P = [0,1,3]

print(jak_dojade(G,P,5,0,2))
print(jak_dojade(G,P,6,0,2))
print(jak_dojade(G,P,3,0,2))