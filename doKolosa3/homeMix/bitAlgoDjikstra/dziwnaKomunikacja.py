from queue import PriorityQueue
# Komunikacja miejska w Pewnym Mieście jest dość dziwnie zorganizowana. 
# Za przejechanie każdego odcinka między dwiema stacjami obowiązuje osobna opłata.
#  Od tej kwoty jest jednak odejmowany całkowity koszt poniesiony od początku podróży (jeśli jest ujemny, po prostu nic się nie płaci).

# Np. na trasie 1-2-3-5 opłaty wyniosą kolejno: 60+20+0, a na trasie 1-4-5 będzie to 120+30

# Mając dane:
# graf połączeń w dowolnej reprezentacji (nieskierowany, ważony)
# numery stacji początkowej i docelowej

# Oblicz minimalny koszt przejechania tej trasy.

def dijkstra(G,s,t):
    q = PriorityQueue()
    n = len(G)
    parent = [-1 for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 0
    q.put((0,s))
    while not q.empty():
        u = q.get()[1]
        if not visited[u]:
            visited[u] = True
            for v,w in G[u]:
                tmp = max(d[u],w)
                if d[v] > tmp:
                    d[v] = tmp
                    parent[v] = u
                q.put((d[v],v))
    return d[t]