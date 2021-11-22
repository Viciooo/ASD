# Żeglarz Henryk mieszka na wysepce pewnego archipelagu. Wszystkie wyspy w tym archipelagu są tak małe,
# że można je reprezentować jako punkty w przestrzeni R2. Pozycje wszystkich wysp dane są jako ciąg
# W = ((x1, y1), … , (xn, yn)). Henryk mieszka na wyspie(x1, y1), ale chce się przeprowadzić na wyspę (xn, yn).
# Normalnie, każdego dnia może przepłynąć na wyspę znajdującą się w odległości najwyżej Z
# (w sensie standardowej odległości euklidesowej), ale może także każdego dnia przepłynąć odległość do 2Z, pod warunkiem,
# że cały następny dzień będzie odpoczywał. Henryk musi zawsze nocować na jakiejś wyspie. Proszę zaproponować (bez implementacji)
# wielomianowy algorytm, który oblicza ile minimalnie dni Henryk potrzebuje, żeby dostać się na swoją docelową wyspę (lub stwierdza,
# że to niemożliwe).

# from queue import PriorityQueue

# def howLongDoesItTake(W,Z):
#     n = len(W)
#     G = [[] for _ in range(n)]
#     for i in range(n):


#     q = PriorityQueue()
#     n = len(G)
#     visited = [False]*n
#     d = [-1]*n

#     q.put(s)
#     d[s] = 0
#     visited[s] = True

#     while not q.empty():
#         u = q.get()
#         for v in G[u]:
#             if not visited[v]:
#                 visited[v] = True
#                 d[v] = d[u]+1
#                 q.put(v)

def d(w1,w2):
    return ((w1[0]-w2[0])**2+(w1[1]-w2[1])**2)**(0.5)

def sailDP(W,Z):
    n = len(W)
    F = [float("inf")]*n
    F[0] = 0
    for i in range(n): #idziemy z i
        for j in range(n): #do j
            if j == i:
                continue
            D = d(W[i],W[j])
            if D <= Z:
                F[j] = min(F[j],F[i]+1)
            elif D <= Z*2:
                F[j] = min(F[j],F[i]+2)
    return False if F[n-1] == float("inf") else F[n-1]

#zł czasowa O(n^2)
#zł pamięciowa O(n)
W = [(0,0),(1,1),(2,2),(4,4),(6,6)]
Z = 3
print(sailDP(W,Z))

#napisać to grafowo jak mi się będzie nudzić choć zł będzie taka sama przez budowę grafu