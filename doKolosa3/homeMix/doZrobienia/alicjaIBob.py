from queue import PriorityQueue
#No co po prostu Djikstra i do domu. 
#Jęśli Alice jedzie pierwsza:

#Relax działa tak że jeśli poprzedni wierzchołek był osiągnięty jako parzysty z koleji 
#to znaczy że obecny jest osiągnięty jako nieparzysty z koleji czyli musimy uwzględnić w relaxie dla wierzchołka v : d[u] + w
#jeśli edges[u] jest odd to teraz ten wierzchołek będzie osiągany jako even czyli uwzględniamy d[u] tylko

#Jeśli Alice jedzie druga to jest na odwrót w sensie zmiana everOrOdd na 1 zmienia o 180 stopni

def relaxModified(u,v,w,d,parent,edges,evenOrOdd):
    if edges[u] % 2 == (evenOrOdd+1)%2 and d[v] > d[u]: #jeśli evenOrOdd == 0 to ten ktoś idzie po nieparzystych
        d[v] = d[u]
        parent[v] = u
        edges[v] = edges[u] + 1

    if edges[u] % 2 == (evenOrOdd)%2 and d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u
        edges[v] = edges[u] + 1

def dijkstraAliceBob(G,evenOrOdd,s,e):
    #G to lista adjacencji składująca tuple (do kąd,cena)
    q = PriorityQueue()
    n = len(G)
    parent = [-1 for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    edges = [None for _ in range(n)]
    edges[s] = 0
    d[s] = 0
    q.put((0,s))
    while not q.empty():
        u = q.get()
        if not visited[u[1]]:
            visited[u[1]] = True
            for i in G[u[1]]:
                relaxModified(u[1],i[0],i[1],d,parent,edges,evenOrOdd)
                q.put((d[i[0]],i[0]))
    return d[e],parent

def solve(G,s,e):
    resOdd, pOdd = dijkstraAliceBob(G,0,s,e)
    resEven, pEven = dijkstraAliceBob(G,1,s,e)
    solution = []
    if resOdd > resEven:
        whoFirst = "B"
        better = pEven
    else:
        whoFirst = "A"
        better = pOdd
    i = e
    while better[i] != -1:
        solution.append(i)
        i = better[i]
    return whoFirst,solution

# E = [[0,1,100],[1,4,100],[4,5,10],[5,3,1000],[3,2,1000],[2,0,10**6],[2,4,20]]
E = [[0,7,30],[0,8,5],[8,2,50],[7,1,10],[1,2,20],[0,2,10],[2,3,3],[3,4,60],[3,5,20],[4,5,5],[5,6,4]]
def convertFromEdgeListToAdjList(E,V):
    G = [[]for _ in range(V)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    return G

G = convertFromEdgeListToAdjList(E,9)
# print(G)

print(solve(G,0,6))