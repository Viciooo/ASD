#Piotr Witek

#zł obliczeniowa O(E*V^2) dla grafów rzadkich lepiej robić to na listach adjacencji
#ale tu nie zamieniam na listę gdyż wiąże się to ze zł pamięciową O(V^2)

#zł pamięciowa O(V)

#Dla każdej krawędzi z a do b takiej że a < b gdzie a i b to nr wierzchołków ustawiam koszt tej krawędzi na inf oczywiście spamiętując
#jaka wartość wcześniej tam była (nie chcemy niszczyć tego grafu) nastepnie szukam najkrótszej ścieżki z a do b. Jeśli wartość < infinity
#to oznacza ze mamy cykl. Procedurę wykonuję dla każdej krawędzi (czyli dla E/2 krawędzi bo "a" musi być mniejsze od "b").


#do poprawki
def minWeightVertex(included, d, n):
    mini, minIndex = float("inf"), -1
    for i in range(n):
        if not included[i] and d[i] < mini:
            mini = d[i]
            minIndex = i
    return minIndex


def dijkstra(G,s,k):
    n = len(G)
    d = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    d[s] = 0
    included = [False for _ in range(n)]
    for i in range(n):
        minVertex = minWeightVertex(included, d, n)
        included[minVertex] = True
        for j in range(n):
            if G[minVertex][j] != -1 and not included[j] and d[j] > d[minVertex] + G[minVertex][j]:
                d[j] = d[minVertex] + G[minVertex][j]
                parent[j] = minVertex
    return d[k],parent

def min_cycle(G):
    n = len(G)
    minParent = []
    minCost = float("inf")
    minEdge = [-1,-1]
    for i in range(n-1):
        for j in range(i+1,n):
        #dla każdej krawędzi takiej że początek jest mniejszy od końca
            if G[i][j] != -1 and i < j:
                tmp = G[i][j]
                G[i][j] = float("inf")
                cost, p = dijkstra(G,i,j)
                if cost + tmp < minCost:
                    minParent = p
                    minCost = cost + tmp
                    minEdge = [i,j]
                    G[i][j] = tmp
    result = []
    i = minEdge[1]
    while i != -1:
        result.append(i)
        i = minParent[i]
    
    return result
G1 = [[-1, 2,-1,-1, 1], #[]
    [ 2,-1, -1, -1,-1],
    [-1, -1,-1, 5,-1],
    [-1, -1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]]

G2 = [[-1, 2,-1,-1, 1],  #[1, 3, 4, 0]
    [ 2,-1, 4, 1,-1],
    [-1, 4,-1, 5,-1],
    [-1, 1, 5,-1, 3],
    [ 1,-1,-1, 3,-1]]

G3 = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],   #[5, 6, 8, 2]
         [4, -1, 8, -1, -1, -1, -1, 11, -1],
         [-1, 8, -1, 7, -1, 4, -1, -1, 2],
         [-1, -1, 7, -1, 9, 14, -1, -1, -1],
         [-1, -1, -1, 9, -1, 10, -1, -1, -1],
         [-1, -1, 4, 14, 10, -1, 2, -1, -1],
         [-1, -1, -1, -1, -1, 2, -1, 1, 6],
         [8, 11, -1, -1, -1, -1, 1, -1, 7],
         [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

# print(min_cycle(G1))
# print(min_cycle(G2))
# print(min_cycle(G3))
# G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#      [4, 0, 8, 0, 0, 0, 0, 11, 0],
#      [0, 8, 0, 7, 0, 4, 0, 0, 2],
#      [0, 0, 7, 0, 9, 14, 0, 0, 0],
#      [0, 0, 0, 9, 0, 10, 0, 0, 0],
#      [0, 0, 4, 14, 10, 0, 2, 0, 0],
#      [0, 0, 0, 0, 0, 2, 0, 1, 6],
#      [8, 11, 0, 0, 0, 0, 1, 0, 7],
#      [0, 0, 2, 0, 0, 0, 6, 7, 0]]

# for i in range(len(G)):
#     for j in range(len(G)):
#         if G[i][j] == 0:
#             G[i][j] = -1

print(dijkstra(G3,0))