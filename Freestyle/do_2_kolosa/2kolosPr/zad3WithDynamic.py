from queue import Queue
#f(i,j) - najnizszy koszt następnych i krawędzi w wierzchołku j
#f(0,j) = 0
#f(i,j) = min(f(i-1,c)+w), c to dzieci j
#O(k*(V+E)+V^2) = O(V^2) k to dł sklejenia

#Pomysł:
#Przechodzę dfsem i w tablicy F zapisuję najkorzystniejsze ścieżki o dł od 1 do k-1 od dzieci do przodu i zwiększam to o koszt krawędzi z parenta do dziecka

class Job:
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end
    def __str__(self):
        return "( " + str(self.start) + " - " + str(self.end) + " )"

def impatientBob(J,n,k):
    G = [[] for _ in range(n)]
    F = [[float("inf") for _ in range(n)] for _ in range(k)]
    for j in range(n):
        F[0][j] = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if J[j].start >= J[i].end:
                G[i].append((j,J[j].start - J[i].end))
                F[1][i] = min(F[1][i],J[j].start - J[i].end)

    visited = [False]*n
    def dfsVisit(u):
        nonlocal G,visited,F
        visited[u] = True
        for v in G[u]:
            if not visited[v[0]]:
                dfsVisit(v[0])
            for i in range(k):
                F[i][u] = min(F[i][u],F[i-1][v[0]]+v[1])

    for i in range(n):
        if not visited[i]:
            dfsVisit(i)
    return min(F[k-1]) if min(F[k-1]) != float("inf") else -1

P1 = [Job(1,2),Job(1,6),Job(4,10),Job(9,12)]
odp1 = 2
k1 = 2

P2 = [Job(0,2),Job(0,7),Job(2,10),Job(9,13),Job(11,13),Job(15,17),Job(18,20),Job(21,25)]
odp2 = 1
k2 = 3

P3 = [Job(1,5),Job(2,6)]
odp3 = -1
k3 = 12

P = [(P1,odp1,k1),(P2,odp2,k2),(P3,odp3,k3)]


def runtests(ez):
    git = True
    for Pi,odp,k in P:
        for elem in Pi:
            print(str(elem),end = " ")
        print()
        ret = ez(Pi,len(Pi),k)
        print("otrzymany wynik:" + str(ret))
        print("oczekiwany wynik:" + str(odp))
        print("git" if ret == odp else "Błąd mordo zmien cos")
        if ret != odp:
            git = False
        print("-----------------------------------")
    if not git:
        print("wynik:   tiny.cc/pudzian")
    else:
        print("wynik:   tiny.cc/pudzianv2")

runtests(impatientBob)