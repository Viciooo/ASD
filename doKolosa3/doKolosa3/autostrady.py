from math import ceil
class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0
        self.parent = self
    def __str__(self):
        return str(self.val)

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def Kruskal(E,max_w,n):
    #krawędzie reprezentowane (u,v,w)
    G = []
    V = [Node(i) for i in range(n)]
    for u,v,w in E:
        G.append([V[u],V[v],w])
    G.sort(key=lambda x: x[2])
    result = []
    for u,v,w in G:
        x = find(u)
        y = find(v)
        if w >= max_w and x != y:
            result.append([u.val,v.val,w])
            union(x,y)
    return result[-1][2] - result[0][2] if DFS(edgeToAdjList(result, n)) else float("inf")


def d(A, i, j):
    return ((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5


def change_to_list(C):
    n = len(C)
    E = []
    for i in range(n):
        for j in range(n):
            if i < j:
                E.append([i, j, ceil(d(C, i, j))])

    return E


def edgeToAdjList(E, n):
    G = [[] for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append([E[i][1], E[i][2]])
        G[E[i][1]].append([E[i][0], E[i][2]])

    return G


def DFS(G):

    def DFSVisit(G, u):
        nonlocal visited
        visited[u] = 1
        for v, _ in G[u]:
            if visited[v] == 0:
                DFSVisit(G, v)

    n = len(G)
    visited = [0 for _ in range(n)]
    DFSVisit(G, 0)

    return bool(min(visited))


def do_stuff(G):
    max_v = len(G)
    E = change_to_list(G)
    E.sort(key=lambda x: x[2])
    n = len(E)
    res = float("inf")
    for i in range(n):
        mini = Kruskal(E, E[i][2], max_v)
        if mini < res:
            res = mini

    return res


G1 = [(10,10),(15,25),(20,20),(30,40)]
odp1 = 7
G2 = [(23,56),(12,120),(45,98),(73,37),(1,101)]
odp2 = 14
G3 = [(23,56),(12,120)]
odp3 = 0
G4 = [(100,100),(100,200),(200,100),(200,200)]
odp4 = 0
G5 = [(100,100),(100,200),(210,100),(210,200)]
odp5 = 10
G6 = [(100,100),(100,200),(200,100),(200,200),(150,151)]
odp6 = 1
print(do_stuff(G6))
