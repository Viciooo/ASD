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

def fromMatrixToList(G):
    n = len(G)
    F = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                F[i].append([j,G[i][j]])
    return F

def reverseIfSbFucksUpList(G):
    for i in range(len(G)):
        for j in G[i]:
            j[0],j[1] = j[1],j[0]


def fromListToMatrix(G):
    #zakładam że lista ma tuple (cena,dokąd)
    n = len(G)
    F = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            F[i][j[1]] = j[0]
    return F



def convertFromEdgeListToAdjList(E,V):
    G = [[]for _ in range(V)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    return G


def convertFromEdgeListToAdjListDirected(E,V):
    G = [[]for _ in range(V)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
    return G