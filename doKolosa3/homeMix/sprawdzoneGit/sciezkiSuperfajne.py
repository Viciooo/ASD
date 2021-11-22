# Dany jest graf ważony G. Ścieżka superfajna, to taka, która jest nie tylko najkrótszą wagowo ścieżką między v i u,
# ale także ma najmniejszą liczbę krawędzi (inaczej mówiąc, szukamy najkrótszych ścieżek w sensie liczby krawędzi wśród
# najkrótszych ścieżek w sensie wagowym). Podaj algorytm, który dla danego wierzchołka startowego s znajdzie superfajne
# ścieżki do pozostałych wierzchołków.

from queue import PriorityQueue
def relax(u,v,w,d,parent,edges):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u
        edges[v] = edges[u]+1
    elif d[v] == d[u] + w and edges[v] > edges[u]+1:
        edges[v] = edges[u]+1
        parent[v] = u

def dijkstraFewestEdges(G,s):
    #G to lista adjacencji składująca tuple (cena, dokąd)
    q = PriorityQueue()
    n = len(G)
    parent = [-1 for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    edges = [float("inf") for _ in range(n)]
    edges[s] = 0
    d[s] = 0
    q.put((0,s))
    while not q.empty():
        u = q.get()
        if not visited[u[1]]:
            visited[u[1]] = True
            for i in G[u[1]]:
                relax(u[1],i[1],i[0],d,parent,edges)
                q.put((d[i[1]],i[1]))
    return parent,d,edges


def reverseIfSbFucksUpList(G):
    for i in range(len(G)):
        for j in G[i]:
            j[0],j[1] = j[1],j[0]

G = [[(1,1),(2,5)],[(1,0),(5,3),(2,4),(1,5)],[(2,3),(6,5)],[(5,1),(3,2),(3,4)],[(2,1),(3,3)],[(2,0),(1,1),(6,2)]]
# Parents: [None, 0, 5, 1, 1, 0] distances: [[0, 0], [1, 1], [8, 2], [6, 2], [3, 2], [2, 1]]
print(dijkstraFewestEdges(G,0))