#zł czasowa O(x*ElogV + V^2) = O(x*ElogV)
#zł pamięciowa O(V*x + V^2)
#zakładając że nie ma ujemnych wag

def fromMatrixToList(G,T):
    n = len(G)
    F = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0 and T[j] != "niebieska":
                F[i].append([j,G[i][j]])
    return F

from queue import PriorityQueue

def getSolution(parent,T,A,i,day):
    if i == A:
        return [A]
    if T[i] != "czerwony":
        return getSolution(parent,T,A,parent[i][day],day+1) + [i]
    else:
        return getSolution(parent,T,A,parent[i][day],day-1) + [i]

def mlodszy_pasjonat(M,A,B,y,D,x,T):
    #y jest useless D też 
    G = fromMatrixToList(M,T)
    Q = PriorityQueue()
    n = len(G)
    parent = [[None for _ in range(x+1)] for _ in range(n)]
    d = [[float("inf") for _ in range(x+1)] for _ in range(n)]
    visited = [[False for _ in range(x+1)] for _ in range(n)]
    d[A][0] = 0
    Q.put((0,A,0))
    # dist,wierzchołek,który dzień trzymanej czerwonej karty
    while not Q.empty():
        _,u,day = Q.get()
        if not visited[u][day]:
            visited[u][day] = True
            for v,w in G[u]:
                if T[v] == "czerwony" and day + 1 > x:
                    continue
                if T[v] != "czerwony" and d[v][max(day-1,0)] > d[u][day] + w:
                    d[v][max(day-1,0)] = d[u][day] + w
                    parent[v][max(day-1,0)] = u
                    Q.put((d[v][max(day-1,0)],v,day))
                elif T[v] == "czerwony" and d[v][day+1] > d[u][day] + w:
                    d[v][day+1] = d[u][day] + w
                    parent[v][day+1] = u
                    Q.put((d[v][day+1],v,day+1))
    day = 0
    for i in range(x+1):
        if d[B][day] > d[B][i]:
            day = i
    return getSolution(parent,T,A,B,day)

from copy import deepcopy
M = [[0,10,0,120,0,0,1],
      [10,0,6,0,0,0,0],
      [0,6,0,7,0,0,0],
      [120,0,7,0,1,0,0],
      [0,0,0,1,0,1,0],
      [0,0,0,0,1,0,1],
      [1,0,0,0,0,1,0]]

T = ["biały","biały","czerwony","czarny","czerwony","czerwony","biały"]

A = 0
B = 3
y = 6
D = 4
x = 0
odp = [0,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

y = 8
x = 1
odp = [0,1,2,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

y = 10
x = 3
odp = [0,6,5,4,3]
print(mlodszy_pasjonat(deepcopy(M),A,B,y,D,x,deepcopy(T)), odp)

