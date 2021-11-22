# Piotr Witek

def nCycleFinder(G,n):
    #lista adjencji
    V = len(G)
    sol = 0
    for i in range(V):
        sol += dfs(G,i,n,V)
        if sol != 0:
            return 1
    return 0
    
def dfs(G,s,n,V):
    visited = [False]*V
    cnt = 0

    def dfsVisit(u,n):
        nonlocal G,visited,s,cnt
        visited[u] = True
        if n == 1:
            for v in G[u]:
                if v == s:
                    cnt += 1
            return
        for v in G[u]:
            if not visited[v]:
                dfsVisit(v,n-1)

    dfsVisit(s,n)
    return cnt

#szukam ścieżki długości n-1 z każdego wierzchołka jesli jeszcze nie znaleźliśmy cyklu, jeśli ścieżka istnieje sprawdzam czy istnieje krawędź
#z ostatniego wierzchołka ścieżki do pierwszego - jeśli tak to mamy cykl
#zł czasowa to O(n^2)
#ale theta(n)
#banalnie proste jest dodanie wypisywania wszystkich cykli dodając do dfsa memo
#oprócz tego można zliczać wszystkie cykle dł n a nie znaleźć jeden
#cnt jest zostawiony zamiast flagi gdyż programem szukałem wszystkich cykli - mozna tu wstawić samą flagę
G = [[1,6],[0,2],[1,3,6],[2,4,5],[3,5],[3,4],[0,2,7],[6]]
print(nCycleFinder(G,4))