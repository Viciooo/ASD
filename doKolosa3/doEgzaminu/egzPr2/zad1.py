def sieve(n):
    arr = []
    if n < 2:
        return []
    else:
        skr = [False] * (n + 1)
        i = 2
        while i * i <= n:
            if not skr[i]:
                j = i * i            
                while j <= n:
                    skr[j] = True
                    j += i
            i += 1
        for i in range(2, n+1):
            if not skr[i]:
                arr.append(i)
    return arr

def binSearch(arr,val):
    n = len(arr)
    low, high, mid = 0, n-1, (n-1)//2
    while low <= high:
        if val < arr[mid]:
            high = mid-1
            mid = (low+high)//2
        elif val > arr[mid]:
            low = mid+1
            mid = (low+high)//2
        else:
            return mid
    return -1


from queue import PriorityQueue

def getColorNum(color):
    if color == "Brun":
        return 1
    else:
        return 0

def getNameOfColor(num):
    if num == 1:
        return "Brun"
    else:
        return "Blond"

def babiarz(G,T,W):
    n = len(T)
    mapOfPrimes = sieve(n)
    F = [[] for _ in range(n)]

    for j,w in G[0]:
        if binSearch(mapOfPrimes,j) != -1:
            F[0].append((j,w))

    for i in range(1,n):
        if binSearch(mapOfPrimes,i) != -1:
            for j,w in G[i]:
                if i > j and T[i] != T[j] and binSearch(mapOfPrimes,j) != -1:
                    F[i].append((j,w))
    
    Q = PriorityQueue()
    d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    d[0] = 0
    d[0] = 0
    Q.put((0,0,W))
    Q.put((0,0,W))
    while not Q.empty():
        _,u,steps = Q.get()
        if not visited[u]:
            visited[u] = True
            for v,w in F[u]:
                if steps >= w:
                    if d[v] > d[u] + w:
                        d[v] = d[u] + w
                        Q.put((d[v],v,steps - w))
    for i in d:
        print(i)
    
    


G1 = [[(1,1),(2,5),(3,11),(4,3)],[(0,1),(3,3),(5,1),(6,1)],[(0,5),(3,3),(5,42)],[(2,3),(1,1),(0,11)],[(0,3)],[(2,42),(1,1)],[(1,1)]]
T1 = ["Łysy","Brun","Brun","Blond","Blond","Blond","Blond"]
W1 = 47
odp1 = [0,3,2]

# G2 = [[(11,21),(8,15),(1,1),(2,5),(3,11),(4,3)],[(0,1),(3,3),(5,1),(6,1)],[(0,5),(3,3),(5,42)],[(2,3),(1,1),(0,11)],[(0,3)],[(2,42),(1,1)],[(1,1)],[(4,1),(8,10),(5,5)],[(0,15),(7,10)],[],[],[(0,21),(7,37)]]
# T2 = ["Łysy","Brun","Blond","Brun","Blond","Blond","Brun","Brun","Blond","Brun","Brun","Blond"]
# W2 = 63
# odp2 = [0,11,7,5]

print(babiarz(G1,T1,W1) == odp1)
# print(babiarz(G2,T2,W2) == odp2)