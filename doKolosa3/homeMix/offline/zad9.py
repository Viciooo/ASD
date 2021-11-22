from copy import deepcopy
#Piotr Witek

#zł obliczeniowa O(E*V^2) dla grafów rzadkich lepiej robić to na listach adjacencji
#ale tu nie zamieniam na listę gdyż wiąże się to ze zł pamięciową O(V^2)

#zł pamięciowa O(V)

#Dla każdej krawędzi z a do b takiej że a < b gdzie a i b to nr wierzchołków ustawiam koszt tej krawędzi na inf oczywiście spamiętując
#jaka wartość wcześniej tam była (nie chcemy niszczyć tego grafu) nastepnie szukam najkrótszej ścieżki z a do b. Jeśli wartość < infinity
#to oznacza ze mamy cykl. Procedurę wykonuję dla każdej krawędzi (czyli dla E/2 krawędzi bo "a" musi być mniejsze od "b").


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
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
G = [[-1, 2,-1,-1, 1],
     [ 2,-1, 4, 1,-1],
     [-1, 4,-1, 5,-1],
     [-1, 1, 5,-1, 3],
     [ 1,-1,-1, 3,-1]]  
LEN = 7


GG = deepcopy( G )
cycle = min_cycle( GG )

print("Cykl :", cycle)


if cycle == []: 
  print("Błąd (1): Spodziewano się cyklu!")
  exit(0)
  
L = 0
u = cycle[0]
for v in cycle[1:]+[u]:
  if G[u][v] == -1:
    print("Błąd (2): To nie cykl! Brak krawędzi ", (u,v))
    exit(0)
  L += G[u][v]
  u = v

print("Oczekiwana długość :", LEN)
print("Uzyskana długość   :", L)

if L != LEN:
  print("Błąd (3): Niezgodna długość")
else:
  print("OK")
  
