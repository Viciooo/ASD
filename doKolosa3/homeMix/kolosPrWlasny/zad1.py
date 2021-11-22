#1) djikstra ale robimy dwuwymiarowych parentów i parent[i][j] = parent j'ty z kolei wierzchołka i
#jeśli relaksujemy wierzchołek to czyścimy parentów i dodajemy nowego 
#jeśli koszt == to dodajemy parenta
#jeśli większy olewamy to
#jesli wierzcholek visited to sprawdzamy czy możliwa relaksacja i tyle(chyba bez sensu)
from queue import PriorityQueue
def dijkstra(G,s):
    q = PriorityQueue()
    n = len(G)
    # parent = [[] for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    countWays = [0 for _ in range(n)]
    countWays[s] = 1
    d[s] = 0
    q.put((0,s))
    while not q.empty():
        u = q.get()[1]
        if not visited[u]:
            visited[u] = True
            for v,w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    # parent[v] = [u]
                    countWays[v] = countWays[u]
                elif d[v] == d[u] + w:
                    # parent[v].append(u)
                    countWays[v] += countWays[u]
                q.put((d[v],v))
    return countWays

# def getPathAmt(parent,u,v,cnt=0):
#     if v == u:
#         return cnt
#     if len(parent[v]) == 0:
#         return -1
#     for i in parent[v]:
#         return getPathAmt(parent,u,i,parent)

def solve(G,u):
    cnt = dijkstra(G,u)
    cnt[u] = 0
    print(cnt)
    return cnt



G1 = [[(2, 10), (4, 10000), (5, 213)], [(4, 5), (5, 98), (0, 123455)], [(3, 987), (4, 111)], [], [(5, 1)], [(3, 444)], [(5, 2)], []]
s1 = 1
odp1 = [1,0,1,1,1,1,0,0]

G2 = [[(1, 1)], [(2, 1)], [(3, 1)], [(4, 1)], [(5, 1)], [(6, 1)], [(7, 1)], [(8, 1)], [(9, 1)], [(10, 1)], [(11, 1)], [(0, 1)]]
s2 = 0
odp2 = [0,1,1,1,1,1,1,1,1,1,1,1]
G3 = [[(1, 100), (2, 2), (3, 3), (4, 4), (5, 2)], [(0, 100), (2, 1)], [(0, 2), (1, 1), (3, 2), (5, 4)], [(0, 3), (2, 2), (4, 3)], [(0, 4), (3, 3), (5, 2)], [(0, 2), (4, 2), (2, 4)]]
s3 = 5
odp3 = [1,2,2,2,1,0]
etst= [(G1,s1,odp1),(G3,s3,odp3)]

random_wrong = ["https://www.youtube.com/watch?v=Gz0rVvVG4jY  nie jestes tu pudzianem(bad)",
        "https://www.youtube.com/watch?v=UlCCg93okG0  tym gosciem nie jestes(bad)",
        "https://www.youtube.com/watch?v=8AwVRlXsxlA  nawet jakbym wygral, to by nic nie dalo (bad)",
        "https://www.youtube.com/watch?v=lj4EP3i_nkc  tak sie nie robi(bad)",
        "Tak dziala twoj program: https://www.youtube.com/watch?v=80Ms8hoqm6s - nie dziala",
        "https://www.youtube.com/watch?v=giT3DZmy2tk tu nie pojedziesz bo masz zle",
        "https://www.youtube.com/watch?v=blA6y6cvcvY ona by to lepiej zrobila takie realia (źle)",
        "https://www.youtube.com/watch?v=3C-gs1fwJC4  do tego nie trzeba okreslac czy masz zle",
        "https://www.youtube.com/watch?v=2rEcXkJggWs  jakies ciastka czy placki, a ty masz źle",
        "https://www.youtube.com/watch?v=j_59a20ea3A  cos jest nie tak w kodzie",
        "https://www.youtube.com/watch?v=ptr7WSfE1wg  JAAAPIERDDOLEEEE, nie dziala",
        "https://www.youtube.com/watch?v=tKP1pxF7J5Q  tak sie nie robi"]


random_good = [ "https://www.youtube.com/watch?v=UhqaHD1hCJc gites co moge powiedziec",
        "https://www.youtube.com/watch?v=_SrJfyQPQlk  Jak zapomniec tak dobry wynik(dobrze)",
        "https://www.youtube.com/watch?v=TOk0wqcU3hs juz za dzieciaka chcialem czarne lamborghini, z takim programem tez mozesz miec (good), oversexualised teledysk",
        "https://www.youtube.com/watch?v=wGeFVtLo1RA  you know the drill AGH gurom(good)",
        "https://www.youtube.com/watch?v=RPIQNktKfOw     POLONEZZZZZZZ(good)",
        "https://www.youtube.com/watch?v=KOY_05KwJYk bo jestes ty i masz dobrze zrobiony ten test",
        "https://www.youtube.com/watch?v=GXzPgIxlrjg  wszystko gites"
        ]

from random import randint
def runtests(f):
    l = 0
    flag = False
    for G,s,odp in etst:
        print("test nr " + str(l) + " robi brrr")
        oo = f(G,s)
        l+=1
        if odp != oo:
            flag = True
            print("zle")
        else:
            print("dobnrze")
    if flag:
        i = randint(0,len(random_wrong))
        print(random_wrong[i])
    else:
        i = randint(0,len(random_good))
        print(random_good[i])

runtests(solve)