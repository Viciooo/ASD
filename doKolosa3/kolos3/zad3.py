from zad3testy import runtests
from zad3EK    import edmonds_karp
#Piotr Witek
#Pomysł:
#Puszczam floyda aby uzyskać najkrótsze ścieżki pomiędzy każdą parą, następnie wybieram tylko ścieżki z B do G takie że ich odległość jest >= D
#tworzę sztuczny giga source i giga sink i dajemy połączenia tylko do wierzchołków które biorą udział w sieci residualnej następnie odpalam e. Karpa

#zł czasowa O(VE^2) zł edmonda karpa
#zł pamięciowa O(V^2)

#uzasadnienie poprawności:
#Floyd gwarantuje najkrótsze ścieżki z każdego do każdego więc ta częśc jest spełniona, Edmond Karp wyznaczy największe skojarzenie w grafie G
#Każdy wierzchołek można użyć wielokrotnie jako środek "trasy" więc to nic nie popsuje


def floydWarshall(G):
    #G to macierz
    n = len(G)
    D = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                D[i][j] = G[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D
    
def BlueAndGreen(T, K, D):
    dist = floydWarshall(T)
    n = len(T)
    G = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            if K[i] == 'B' and K[j] == 'G' and dist[i][j] >= D:
                G[i][j] = 1
    #n to source
    #n+1 to sink
    for i in range(n):
        if max(G[i]) > 0:
            G[n][i] = 1
            G[i][n+1] = 1

    return edmonds_karp(G,n,n+1)

runtests( BlueAndGreen ) 
