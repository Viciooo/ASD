from queue import PriorityQueue

def convertFromEdgeListToAdjList(E,n):
    G = [[]for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    return G

def getSolution(parent,idxG,idxW):
    if idxW == -1:
        return []
    return getSolution(parent,parent[idxG][idxW],idxW-1) + [idxG]

def letters(L,E,W):
    Q = PriorityQueue()
    m = len(W)
    n = len(L)
    G = convertFromEdgeListToAdjList(E,n)
    d = [[float("inf") for _ in range(m)] for _ in range(n)]
    parent = [[None for _ in range(m)] for _ in range(n)]
    for i in range(n):
        if L[i] == W[0]:
            Q.put((0,0,i))
            d[i][0] = 0
            #(odległość d,index w W,index wierzchołka w G)

    while not Q.empty():
        _,idxW,idxG = Q.get()
        if idxW == m - 1:
            break
        for v,w in G[idxG]:
            if L[v] == W[idxW+1] and d[v][idxW+1] > d[idxG][idxW] + w:
                d[v][idxW+1] = d[idxG][idxW] + w
                parent[v][idxW+1] = idxG
                Q.put((d[v][idxW+1],idxW+1,v))

    _min, idxG = float("inf"), None
    for i in range(n):
        if L[i] == W[m-1] and _min > d[i][m-1]:
            idxG = i
            _min = d[i][m-1]
    if idxG != None:
        solution = getSolution(parent,idxG,m-1)
    return _min,solution if _min != float("inf") else -1

L = ["k","k","o","o","t","t"]
E = [(0,2,2),(1,2,1),(1,4,3),(1,3,2),(2,4,5),(3,4,1),(3,5,3)]
W = "kto"
print(letters(L,E,W))

#O(E*k*log(V)) k - dł słowa