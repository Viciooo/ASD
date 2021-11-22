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
def Kruskal(G,n):
    #krawędzie reprezentowane (u,v,w)
    Graph = []
    V = [Node(i) for i in range(n)]
    for i in G:
        Graph.append([V[i[0]],V[i[1]],i[2]])
    Graph.sort(key=lambda x: x[2])
    result = []
    E = 0
    i = 0
    while E < n - 1:
        u, v, w = Graph[i]
        x = find(u)
        y = find(v)
        if x != y:  #nie ma cyklu
            E += 1
            result.append(w)
            union(x,y)
        i += 1
    return result

def preprocess(arr,listOfRad):
    #arr to lista pkt, a listOfRad to lista indeksów miast z odbiornikami
    E = []
    n = len(arr)
    for i in range(n):
        x, y = arr[i][0], arr[i][1]
        for j in range(n):
            if i != j:
                a, b = arr[j][0], arr[j][1]
                if i in listOfRad and j in listOfRad:
                    d = 0
                else:
                    d = ((x-a)**2 + (y-b)**2)**(0.5)
                E.append((i,j,d))
    #wynik to krawędź o maksymalnej wadze w MST
    return max(Kruskal(E,n))

arr = [(1,2),(3,3),(4,3),(4,0),(6,2),(7,0)]
radOdb = [3,5]
print(preprocess(arr,radOdb))