from queue import Queue
#zł czasowa O(V*(V+E))
#zł pamięciowa O(V)

#f(i,j) - najnizszy koszt następnych j krawędzi w wierzchołku i
#f(i,0) = 0
#f(i,j) = min(f(c,j-1)+w), c to dzieci i 
#O(k*(V+E)+V^2) = O(V^2) k to dł sklejenia

class Job:
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end
    def __str__(self):
        return "( " + str(self.start) + " - " + str(self.end) + " )"

def impatientBob(J,n,k):
    G = [[] for _ in range(n)]

    for i in range(n-1):
        for j in range(i+1,n):
            if J[j].start >= J[i].end:
                G[i].append((j,J[j].start - J[i].end))

    visited = [False]*n
    minCost = float("inf")
    def dfsVisit(u,q,length,cost):
        nonlocal G,visited,minCost
        visited[u] = True
        if length == k:
            if minCost > cost and cost >= 0:
                minCost = cost
            length -= 1
            cost -= q.get()
            
        for v in G[u]:
            q.put(v[1])
            dfsVisit(v[0],q,length+1,cost+v[1])

    for i in range(n):
        if not visited[i]:
            q = Queue()
            dfsVisit(i,q,1,0)

    return minCost if minCost != float("inf") else -1

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