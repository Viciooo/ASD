#f(i,j) - najdłuższa ścieżka kończąca się w i,j
from queue import Queue
import queue
def find(T):
    m = len(T)
    n = len(T[0])
    F = [[-1 for _ in range(n)] for _ in range(m)]
    q = Queue()
    for i in range(m):
        for j in range(n):
            if F[i][j] == -1:
                q.put((i,j,1))
                F[i][j] = 1
                while not q.empty():
                    r,c,k = q.get()
                    if r > 0 and T[r-1][c] > T[r][c]:
                        q.put((r-1,c,k+1))
                        F[r-1][c] = max(F[r-1][c],k+1)
                    if c > 0 and T[r][c-1] > T[r][c]:
                        q.put((r,c-1,k+1))
                        F[r][c-1] = max(F[r][c-1],k+1)
                    if r < m-1 and T[r+1][c] > T[r][c]:
                        q.put((r+1,c,k+1))
                        F[r+1][c] = max(F[r+1][c],k+1)
                    if c < n-1 and T[r][c+1] > T[r][c]:
                        q.put((r,c+1,k+1))
                        F[r][c+1] = max(F[r][c+1],k+1)
    for i in F:
        print(i)

T = [[10,10,10,20],
     [8,10,2,3],
     [6,4,3,6]]
find(T)