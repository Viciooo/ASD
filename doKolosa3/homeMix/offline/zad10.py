from copy import deepcopy
from queue import PriorityQueue
#zł obliczeniowa O(ElogV)
#zł pamięciowa O(V)
#Idea:
#Djikstr tyle że wartość d wierzchołka jest równa minimum z wartości poprzedniego wierzchołka i wagi krawędzi po której przeszliśmy do nowego wierzchołka 
#W pierwszej kolejności chcemy przetwarzać wierzchołki o jak największej odległosci gdyż wtedy będziemy mieli największą możliwą przepustowość.
#Aby nie modyfikować djikstry zbyt mocno a osiągnąć to co chcemy wystarczy wrzucać do kolejki wierzchołki z prio -d[v]

def max_extending_path( G, s, t ):
  n = len(G)
  q = PriorityQueue()
  visited = [False for _ in range(n)]
  parent = [None for _ in range(n)]
  d = [0 for _ in range(n)]
  d[s] = float("inf")
  q.put([0,s])
  # [klucz,wierzchołek]
  # rzeczywista waga = min(krawędź do wierzchołka,waga wierzchołka z którego idziemy)
  while not q.empty():
    u = q.get()[1]
    if not visited[u]:
      visited[u] = True
      for v,w in G[u]:
        mini = min(d[u],w)
        if d[v] < mini:
          parent[v] = u
          d[v] = mini
        q.put([-d[v],v])
  return getSolution(parent,s,t)
  
  
def getSolution(parent,s,t):
  if t == s:
    return [s]
  return getSolution(parent,s,parent[t])+[t]
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")
  
