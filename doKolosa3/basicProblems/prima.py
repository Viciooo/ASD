from queue import PriorityQueue

def prim(G):
    #graf reprezentowany jako lista adjacencji
    V = len(G)
    q = PriorityQueue()
    cost = [float("inf") for _ in range(V)]
    parent = [-1 for _ in range(V)]
    result = []
    q.put((0,0))
    while not q.empty():
        w,v = q.get()
        if cost[v] == float("inf"):
            cost[v] = w
            for i,edge in G[v]:
                if cost[i] == float("inf"):
                    parent[i] = v
                    q.put((edge,i))

    for i in range(V-1,0,-1):
        if parent[i] != -1:
            result.append([parent[i],i,cost[i]])
    result.sort()
    return result


E = [[0,5,3],[0,1,6],[0,2,12],[1,2,4],[1,3,5],[2,4,1],[2,5,10],[3,5,2],[4,5,7]]

def convertFromEdgeList(E,V):
    G = [[]for _ in range(V)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    return G

G = convertFromEdgeList(E,6)
print(prim(G))

#prim bez kolejki można zrobić na tablicy adjacencji branie minimum i tyle