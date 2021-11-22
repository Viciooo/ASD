import queue,sys
class Node:
    def __init__(self,name):
        self.L = None
        self.R = None
        self.name = name

def fillSolution(S,n,root,sol,path=""):
    if root.L == None and root.R == None:
        for i in range(n):
            if root.name == S[i]:
                sol[i] = path
        return
    fillSolution(S,n,root.L,sol,path+"1")
    fillSolution(S,n,root.R,sol,path+"0")

def huffman(S,F):
    q = queue.PriorityQueue()
    n = len(S)
    for i in range(n):
        q.put((F[i],Node(S[i])))
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        c = Node(None)
        c.L = a[1]
        c.R = b[1]
        q.put((a[0]+b[0],c))
    sol = [None for _ in range(n)]
    root = q.get()
    root = root[1]
    fillSolution(S,n,root,sol)
    cnt = 0
    for i in range(n):
        cnt += F[i]*len(sol[i])
        print(S[i]," : ",sol[i])
    print("dlugosc napisu: ",cnt)

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]
huffman(S,F)