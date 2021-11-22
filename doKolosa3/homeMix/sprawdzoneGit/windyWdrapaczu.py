# Wieżowiec ma 100 pięter i n wind, nie ma natomiast schodów. Każda winda posiada listę pięter, 
# do których dojeżdża i prędkość w sekundach na piętro.
# Jesteśmy na piętrze i, chcemy się dostać na piętro j. 
# Ile minimalnie sekund musimy spędzić w windach, aby tam dotrzeć?

#zł obliczeniowa O(m*V+ElogV)
#zł pamięciowa O(V^2)
from queue import PriorityQueue
def relax(u,v,w,d,parent):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        parent[v] = u

def preprocess(W):
    #zakładam strukturę w stylu W = [([p1,p2...,pI],v na piętro dla windy 0),...)]
    #stworzę Graf w postacji listy adjacencji w stylu : [[(o koszcie,do piętra),....],....]
    _max = -1
    m = len(W)
    for i in range(m):
        _max = max(_max,max(W[i][0]))
    n = _max + 1
    G = [[] for _ in range(n)]
    for i in range(m):
        for j in range(len(W[i][0])-1):
            G[W[i][0][j]].append((W[i][1]*abs(W[i][0][j]-W[i][0][j+1]),W[i][0][j+1]))
            G[W[i][0][j+1]].append((W[i][1]*abs(W[i][0][j]-W[i][0][j+1]),W[i][0][j]))
            #robię graf nieskierowany - jako wierzchołki traktuję nr pięter a jako krawędzie czy można dostać się bezpośrednio i o jakim koszcie
    return G

def dijkstra(G,i,j):
    #G to lista adjacencji składująca tuple (cena, do kąd)
    q = PriorityQueue()
    n = len(G)
    parent = [-1 for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    d[i] = 0
    q.put((0,i))
    while not q.empty():
        u = q.get()
        if not visited[u[1]]:
            visited[u[1]] = True
            for i in G[u[1]]:
                relax(u[1],i[1],i[0],d,parent)
                q.put((d[i[1]],i[1]))
    return d[j]

def solve(W,i,j):
    return dijkstra(preprocess(W),i,j)
    
W = [([1,2,3],2),([1,4],1),([0,1,4],7)]
print(solve(W,3,4)) #7
print(solve(W,0,4)) #10