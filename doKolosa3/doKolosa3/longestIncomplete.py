class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.used = 0

def find(root,key):
    while root != None and key != root.key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
    return root

def insert(root,key):
    #p będzie parentem roota przydatnym jeśli element o zadanym kluczu nie występuje w drzewie
    p = None
    while root != None and key != root.key:
        if key < root.key:
            p = root
            root = root.left
        else:
            p = root
            root = root.right

    if root != None: #znaleziono element o kluczy key
        return False

    else:
        x = BSTNode(key)
        x.parent = p
        if key < p.key:
            p.left = x
        else:
            p.right = x
    return True

def solve(A,k):
    #zł obliczeniowa n*logk
    root = BSTNode(A[0])
    n = len(A)
    for i in range(1,n):
        insert(root,A[i])
    start = stop = 0
    #od start do stop jeśli są oba zera to bierzemy tylko element zerowy
    _max = 0
    cnt = 0
    while stop != n:
        while cnt != k:
            if stop == n:
                break
            z = find(root,A[stop])
            if z.used == 0:
                cnt += 1
            z.used += 1
            stop += 1
        while cnt == k:
            z = find(root,A[start])
            z.used -= 1
            if z.used == 0:
                cnt -= 1
            start += 1
        _max = max(stop - start,_max)
    return _max

A = [1,100,5,100,1,5,1,5]

print(solve(A,3))