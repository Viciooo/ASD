# Zadanie 4. (skojarzenie na drzewie) Prosze podac algorytm, który majac na wejsciu drzewo oblicza
# skojarzenie o maksymalnej licznosci. Czy algorytm dalej bedzie działac jesli kazda krawedz bedzie miec
# dodatnia wage i szukamy skojarzenia o maksymalnej sumie wag?

#zakładam że dostaję na wejściu zwykły graf G w postaci listy adjacencji i wierzchołek root
def solution(root,G):
    n = len(G)
    f = [0 for _ in range(n)]#braliśmy krawędź do tego wierzchołka
    g = [0 for _ in range(n)]#nie bralismy
    def dfsVisit(root):
        maxi = 0
        for v,w in G[root]:
            dfsVisit(v)
            g[root] += f[v]
            f[root] += f[v]
            maxi = max(maxi,g[v]-f[v]+w)
        f[root] += maxi
    dfsVisit(root)
    return f,g

G = [[[1,1],[2,1]],[],[[3,1],[4,5]],[[5,1]],[],[[6,1]],[]]
root = 0
print(solution(root,G))
#pewnie needs further testing