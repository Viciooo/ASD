from queue import Queue

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

def enlarge(G,s,t):
    ds = bfs(G,s)
    dt = bfs(G,t)
    n = len(G)
    lenOfPath = ds[t]
    arr = [[] for _ in range(lenOfPath+1)]
    for i in range(n):
        if ds[i] + dt[i] == lenOfPath:
            arr[ds[i]].append(i)
    
    for i in range(1,lenOfPath+1):
        if len(arr[i]) == 1 and len(arr[i-1]) == 1:
            return (arr[i-1][0],arr[i][0])
    return None

G1 = [ [1, 2], 
       [0, 2],
       [0, 1] ] 
s1 = 0
t1 = 2
r1 = (0,2)


G2 = [ [1,4],  # 0
       [0,2],  # 1
       [1,3],  # 2
       [2,5],  # 3
       [0,5],  # 4
       [4,3]]  # 5
s2 = 0
t2 = 3
r2 = None

s3 = 0
t3 = 2
r3 = [(0,1),(1,2)]

G4 = [ [1,4,3],  # 0
       [0,2],    # 1
       [1,3],    # 2
       [2,5,0],  # 3
       [0,5],    # 4
       [4,3]]    # 5
s4 = 0
t4 = 2
r4 = None

        

TESTS = [(G1,s1,t1,r1),
         (G2,s2,t2,r2),
         (G2,s3,t3,r3),
         (G4,s4,t4,r4)
        ]



def runtests( f ):
  OK = True
  for (G,s,t,r) in TESTS:
    print("----------------------")
    print("G: ", G )
    print("s: ", s )    
    print("t: ", t )
    print("oczekiwany wynik: ", r)
    sol = f(G,s,t)
    print("uzyskany wynik  : ", sol)
    if not( (sol == r) or (sol in r) ):
      print("PROBLEM!!!!!!")
      OK = False
     
  print("----------------------")
  if not OK:
    print("PROBLEMY!")
  else:
    print("OK")

runtests(enlarge)