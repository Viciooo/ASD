#zł obliczeniowa O((wk)^2 + wk)
#zł pamięciowa O((wk)^2)
#Pomysł z racji na to że wagi są niezależne od grafu oraz stosunkowo nie duże zwłaszcza po podzieleniu przez 5 używam ala-dijkstry-BFS gdyż ma mniejszą złożoność
#rozdzielam wierzchołki tak jak opisane na dole 

from zad2testy import runtests
from queue import Queue

def robot( L, A, B ):
    w = len(L)
    k = len(L[0])
    visited = [[[False for _ in range(16)] for _ in range(k)] for _ in range(w)]
    #[prawo,lewo,góra,dół|prawo 1 prędkość,lewo 1 prędkość,góra 1 prędkość,dół 1 prędkość|prawo 2 prędkość,lewo 2 prędkość,góra 2 prędkość,dół 2 prędkość|prawo pozostałe prędkość,lewo pozostałe prędkość,góra pozostałe prędkość,dół pozostałe prędkość]
    #przeskaluję wagi krawędzi wszystkie dzieląc przez 5 
    #teraz wynoszą 12,9,8,6
    Q = Queue()
    d = [[[float("inf") for _ in range(16)] for _ in range(k)] for _ in range(w)]
    Q.put((1,(A[1],A[0],0),(A[1],A[0],0),0))
    d[A[1]][A[0]][0] = 0
    #(pozostała waga,wierzchołek(x,y,typ chodzenia),wierzchołek z którego przyszliśmy(x,y,typ chodzenia),waga krawędzi którą przyszliśmy)
    while not Q.empty():
        w1,u,last,edge = Q.get()
        w1 -= 1
        if w1 == 0:
            x, y, wayU = u
            if visited[x][y][wayU]:
                continue
            visited[x][y][wayU] = True
            d[x][y][wayU] = d[last[0]][last[1]][last[2]]+(edge*5)
            if (y,x) == B:
                break
            if wayU == 0:
                if not visited[x][y][2]:
                    Q.put((9,(x,y,2),u,9))

                if not visited[x][y][3]:
                    Q.put((9,(x,y,3),u,9))

                if y + 1 < k and L[x][y+1] != "X" and not visited[x][y+1][4]:
                    Q.put((12,(x,y+1,4),u,12))

            elif wayU == 1:
                if not visited[x][y][2]:
                    Q.put((9,(x,y,2),u,9))

                if not visited[x][y][3]:
                    Q.put((9,(x,y,3),u,9))

                if y - 1 >= 0 and L[x][y-1] != "X" and not visited[x][y-1][5]:
                    Q.put((12,(x,y-1,5),u,12))
            
            elif wayU == 2:
                if not visited[x][y][0]:
                    Q.put((9,(x,y,0),u,9))

                if not visited[x][y][1]:
                    Q.put((9,(x,y,1),u,9))

                if x - 1 >= 0 and L[x-1][y] != "X" and not visited[x-1][y][6]:
                    Q.put((12,(x-1,y,6),u,12))
            
            elif wayU == 3:
                if not visited[x][y][0]:
                    Q.put((9,(x,y,0),u,9))

                if not visited[x][y][1]:
                    Q.put((9,(x,y,1),u,9))

                if x + 1 < w and L[x+1][y] != "X" and not visited[x+1][y][7]:
                    Q.put((12,(x+1,y,7),u,12))
            #########
            elif wayU == 4:
                if not visited[x][y][2]:
                    Q.put((9,(x,y,2),u,9))

                if not visited[x][y][3]:
                    Q.put((9,(x,y,3),u,9))
                
                if y + 1 < k and L[x][y+1] != "X" and not visited[x][y+1][8]:
                    Q.put((8,(x,y+1,8),u,8))#y
            
            elif wayU == 5:
                if not visited[x][y][2]:
                    Q.put((9,(x,y,2),u,9))

                if not visited[x][y][3]:
                    Q.put((9,(x,y,3),u,9))
                
                if y - 1 >= 0 and L[x][y-1] != "X" and not visited[x][y-1][9]:
                    Q.put((8,(x,y-1,9),u,8))#y
            
            elif wayU == 6:
                if not visited[x][y][0]:
                    Q.put((9,(x,y,0),u,9))

                if not visited[x][y][1]:
                    Q.put((9,(x,y,1),u,9))

                if x - 1 >= 0 and L[x-1][y] != "X" and not visited[x-1][y][10]:
                    Q.put((8,(x-1,y,10),u,8))
            
            elif wayU == 7:
                if not visited[x][y][0]:
                    Q.put((9,(x,y,0),u,9))

                if not visited[x][y][1]:
                    Q.put((9,(x,y,1),u,9))

                if x + 1 < w and L[x+1][y] != "X" and not visited[x+1][y][11]:
                    Q.put((8,(x+1,y,11),u,8))
            #################
            elif wayU == 8:
                if not visited[x][y][2]:
                    Q.put((9,(x,y,2),u,9))

                if not visited[x][y][3]:
                    Q.put((9,(x,y,3),u,9))
                
                if y + 1 < k and L[x][y+1] != "X" and not visited[x][y+1][12]:
                    Q.put((6,(x,y+1,12),u,6))#y
            
            elif wayU == 9:
                if not visited[x][y][2]:
                    Q.put((9,(x,y,2),u,9))

                if not visited[x][y][3]:
                    Q.put((9,(x,y,3),u,9))
                
                if y - 1 >= 0 and L[x][y-1] != "X" and not visited[x][y-1][13]:
                    Q.put((6,(x,y-1,13),u,6))#y
            
            elif wayU == 10:
                if not visited[x][y][0]:
                    Q.put((9,(x,y,0),u,9))

                if not visited[x][y][1]:
                    Q.put((9,(x,y,1),u,9))

                if x - 1 >= 0 and L[x-1][y] != "X" and not visited[x-1][y][14]:
                    Q.put((6,(x-1,y,14),u,6))
            
            elif wayU == 11:
                if not visited[x][y][0]:
                    Q.put((9,(x,y,0),u,9))

                if not visited[x][y][1]:
                    Q.put((9,(x,y,1),u,9))

                if x + 1 < w and L[x+1][y] != "X" and not visited[x+1][y][15]:
                    Q.put((6,(x+1,y,15),u,6))
            ##########
            elif wayU == 12:
                if not visited[x][y][2]:
                    Q.put((9,(x,y,2),u,9))

                if not visited[x][y][3]:
                    Q.put((9,(x,y,3),u,9))
                
                if y + 1 < k and L[x][y+1] != "X" and not visited[x][y+1][12]:
                    Q.put((6,(x,y+1,12),u,6))#y
            
            elif wayU == 13:
                if not visited[x][y][2]:
                    Q.put((9,(x,y,2),u,9))

                if not visited[x][y][3]:
                    Q.put((9,(x,y,3),u,9))
                
                if y - 1 >= 0 and L[x][y-1] != "X" and not visited[x][y-1][13]:
                    Q.put((6,(x,y-1,13),u,6))#y
            
            elif wayU == 14:
                if not visited[x][y][0]:
                    Q.put((9,(x,y,0),u,9))

                if not visited[x][y][1]:
                    Q.put((9,(x,y,1),u,9))

                if x - 1 >= 0 and L[x-1][y] != "X" and not visited[x-1][y][14]:
                    Q.put((6,(x-1,y,14),u,6))
            
            elif wayU == 15:
                if not visited[x][y][0]:
                    Q.put((9,(x,y,0),u,9))

                if not visited[x][y][1]:
                    Q.put((9,(x,y,1),u,9))

                if x + 1 < w and L[x+1][y] != "X" and not visited[x+1][y][15]:
                    Q.put((6,(x+1,y,15),u,6))

        elif w1 > 0:
            Q.put((w1,u,last,edge))
    _min = min(d[B[1]][B[0]])


    return _min if _min != float("inf") else None


runtests( robot )

