from zad2testy import runtests
#zł czasowa O(nk^2)
#zł pamięciowa w sumie to O(nk)
#plis dajcie prostsze drzewo na egzaminie ja nie plagiatowicz
class Node:
    def __init__( self ):
        self.left    = None  # lewe podrzewo
        self.leftval = 0     # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right   = None  # prawe poddrzewo
        self.rightval= 0     # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X       = None  # miejsce na dodatkowe dane

def initTree(T,k):
    if T != None:
        T.X = [-float("inf") for _ in range(k+1)]
        T.X[0] = 0
        initTree(T.left,k)
        initTree(T.right,k)


def fakeTraverse(T,k):
    if T != None:
        fakeTraverse(T.left,k)
        fakeTraverse(T.right,k)
        traverseTree(T,k)

def traverseTree(T,k):
    if T != None and k != 0:
        T.X[1] = max(T.leftval if T.left != None else -float("inf"),T.rightval if T.right != None else -float("inf"))
        for j in range(2,k+1):
            if T.left != None and T.right != None:
                for i in range(j-1):
                    T.X[j] = max(T.X[j],T.left.X[i]+T.leftval + T.right.X[j-i-2]+T.rightval)

            if T.left != None:
                T.X[j] = max(T.X[j],T.left.X[j-1]+T.leftval)
            if T.right != None:
                T.X[j] = max(T.X[j],T.right.X[j-1]+T.rightval)
    
def walk(T):
    if T != None:
        print(T.X)
        walk(T.left)
        walk(T.right)
        
def valuableTree(T,k):
    _max = -float("inf")
    initTree(T,k)
    fakeTraverse(T,k)
    def getSolution(T,k):
        nonlocal _max
        if T != None:
            _max = max(_max,T.X[k])
            getSolution(T.left,k)
            getSolution(T.right,k)
    getSolution(T,k)
    return _max
    
runtests( valuableTree )