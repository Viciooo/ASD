from queue import Queue
#Pomysł: wykorzystuję znany algorytm wyszukiwania średnicy w acyklicznym grafie nieskierowanym.
#Z dowolnego wierzchołka odpalam BFS i wybieram dowolny wierzchołek o najwyższym czasie odwiedzenia i z niego odpalam Bfs
# w ten sposów już mam jeden koniec średnicy a drugi znajdę odpalając z tego wierzchołka Bfs. Cały czas pamiętam tablicę wynikową
#z odpalenia bfs z pierwszego wierchołka średnicy i otrzymuję drugą tablicę odwiedzeń z drugiego końca.
#wierzchołek/bądź w przypadku parzystego V wierzchołki o tych samych czasach odwiedzenia zarówno z jednego jak i drugiego końca to 
#rozwiazanie o które proszono gdyż ze środka średnicy będzie najmniej krawędzi po prawej i po lewej jednocześnie(będą rozłożone najrówniej jak się da)

#zł czasowa O((V+E)*3+V*3) = O(V+E)
#zł pamięciowa O(V)


def bfs(G,s):
    q = Queue()
    n = len(G)
    visited = [False]*n
    d = [-1]*n

    q.put(s)
    d[s] = 0
    visited[s] = True

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u]+1
                q.put(v)
    return d

def best_root(L):
    n = len(L)
    d = bfs(L,0)    #odpalamy z losowego wierzchołka bfs aby znaleźć jeden koniec średnicy
    s = 0
    for i in range(1,n):
        if d[i] > d[s]:
            s = i
    d1 = bfs(L,s)
    s = 0
    for i in range(1,n):
        if d1[i] > d1[s]:
            s = i
    d2 = bfs(L,s)
    for i in range(n):
        if d1[i] == d2[i]:
            return i


L1 = [ [ 2 ], [ 2 ], [ 0, 1, 3], [ 2, 4 ],
       [ 3, 5, 6 ], [ 4 ], [ 4 ] ]
R1 = 3

L2 = [ [ 2, 4 ], [ 3 ], [ 0 ], [ 1, 4 ], [ 0, 3 ] ]
R2 = 4

L3 = [ [ 2, 3 ], [ 3, 4, 5, 6 ], [ 0 ],
       [ 0, 1 ], [ 1 ], [ 1 ], [ 1 ] ]
R3 = 3

L4 = [ [ 2 ], [ 2 ], [ 0, 1, 3, 4, 5, 6 ],
       [ 2 ], [ 2 ], [ 2 ], [ 2 ] ]
R4 = 2

TESTS = [ (L1,R1), (L2,R2), (L3,R3), (L4,R4) ]
         

def runtests( f ):
    OK = True
    for (A,R) in TESTS:
        res = f(A)
        print("----------------------")
        print( "A =", A )
        print( "oczekiwany wynik =", R )
        print( "otrzymany wynik  =", res )
        
        if res != R:
            print( "Blad!" )
            OK = False
    print("----------------------")

    if OK:
        print( "OK!" )
    else:
        print( "Bledy!" )

runtests(best_root)