from queue import Queue


def bricks(A):
    #zakładając że możemy niszczyć A
    A.sort()

    n = len(A)
    q = Queue() #kolejka właściwa
    p = Queue() #kolejka na następne poziomy
    C = [A[0]]
    tmp1 = None
    visited = [False for _ in range(n)]
    visited[0] = True
    for i in range(1,n):
        if A[i][0] == C[-1][1]:
            C[-1][1] = A[i][1]
            visited[i] = True
        elif A[i][0] > C[-1][1]:
            C.append(A[i])
            visited[i] = True
    for i in range(len(C)):
        q.put(C[i])
    for i in range(1,n):
        if not visited[i]:
            p.put(A[i])

    while not p.empty():
        tmp = p.get()
        if tmp1 != None and tmp1[0] < tmp[0] and tmp1[1] >= tmp[1]:
            q.put(tmp)
        else:
            while not q.empty():
                tmp1 = q.get()
                if tmp1[0] < tmp[0] and tmp1[1] >= tmp[1]:
                    q.put(tmp)
                    tmp1 = [tmp[1],tmp1[1]]
                    break
        if q.empty():
            return False
    return True

if __name__ == "__main__":
    K = [[2,4],[5,7],[3,6],[4,5],[10,20],[12,14],[13,19]]   #false
    J = [[2,4],[5,7],[3,6],[4,5],[10,20],[12,14],[15,19]]   #true
    print(bricks(K))

#zł czasowa dyktowana przez sortowanie O(nlong)
#zł pamięciowa O(n)