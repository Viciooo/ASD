# Dostajemy na wejściu listę trójek (miastoA, miastoB, koszt). 
# Każda z nich oznacza, że możemy zbudować drogę między miastem A i B za podany koszt. 
# Ponadto, w dowolnym mieście możemy zbudować lotnisko za koszt K, niezależny od miasta. 
# Na początku w żadnym mieście nie ma lotniska, podobnie między żadnymi dwoma miastami nie ma wybudowanej drogi.
# Naszym celem jest zbudować lotniska i drogi za minimalny łączny koszt, tak aby każde miasto miało dostęp do lotniska.
# Miasto ma dostęp do lotniska, jeśli:
# 1) jest w nim lotnisko, lub
# 2) można z niego dojechać do innego miasta, w którym jest lotnisko

# Jeżeli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, należy wybrać to z największą ilością lotnisk.

#zł obliczeniowa O(ElogE)
#zł pamięciowa O(E)
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
def solve(G,n,K):
    #krawędzie reprezentowane (u,v,w)
    Graph = []
    V = [Node(i) for i in range(n)]
    for i in G:
        Graph.append([V[i[0]],V[i[1]],i[2]])
    Graph.sort(key=lambda x: x[2])
    result = []
    E = 0
    i = 0
    cost = 0
    SS = n

    while i < n:
        u, v, w = Graph[i]
        x = find(u)
        y = find(v)
        if x != y and w < K:  #nie ma cyklu
            E += 1
            result.append([u,v,w])
            cost += w
            union(x,y)
            SS -= 1
        i += 1
    return cost + K*SS,SS

# E = [(0,1,2),(0,3,1),(0,2,4),(2,4,3),(2,5,2),(4,5,7),(1,3,1)]   #(10, 2)
# K = 3
# print(solve(E,6,K))
test = [(0,1,2),(1,3,8),(2,3,9),(1,2,4),(1,4,7),(3,4,5),(0,2,3)] 
k=6
print(solve(test,5,k))