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

#dostajemy na wejściu listę KRAWĘDZI
def Kruskal(E,n):
    G = []
    V = [Node(i) for i in range(n)]
    for u,v,w in E:
        G.append([V[u],V[v],w])
    G.sort(key=lambda x: x[2])
    result = []
    for u,v,w in G:
        x = find(u)
        y = find(v)
        if x != y:
            result.append([u.val,v.val,w])
            union(x,y)
    result.sort()
    return result


V = 6
G = [[0,5,3],[0,1,6],[0,2,12],[1,2,4],[1,3,5],[2,4,1],[2,5,10],[3,5,2],[4,5,7]]
G1 = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)]
print(Kruskal(G,V))
#zł obliczeniowa O(ElogE)
#zł pamięciowa O(E)