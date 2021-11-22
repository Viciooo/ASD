class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.idx = 1
    def __str__(self):
        return str(self.key) +","+str(self.idx)

def getMin(root):
    while root.left != None:
        root = root.left
    return root

def getMax(root):
    while root.right != None:
        root = root.right
    return root

def inorderTreeWalk(root):
    if root != None:
        inorderTreeWalk(root.left)
        print(root)
        inorderTreeWalk(root.right)

def find(root,key):
    while root != None and key != root.key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
    return root

def insert(root,key):
    if find(root,key) != None:
        return False
    p = None
    while root != None and key != root.key:
        p = root
        p.idx += 1
        if key < root.key:
            root = root.left
        else:
            root = root.right
        
    else:
        x = BSTNode(key)
        x.parent = p
        if key < p.key:
            p.left = x
        else:
            p.right = x
    return True

def getKthSmallestElement(root,k):
    if root == None:
        return BSTNode("błąd")

    if root.left == None:
        leftSide = 0
    else:
        leftSide = root.left.idx

    if leftSide + 1 == k:
        return root
    if leftSide >= k:
        return getKthSmallestElement(root.left,k)
    if leftSide < k:
        return getKthSmallestElement(root.right,k-leftSide-1)
    if k == 1:
        return getMin(root)

def getPrev(root):
    if root.left != None:
        return getMin(root.left)
    y = root.parent
    while y != None and root != y.right:
        root = y
        y = y.parent
    return y

def getNext(root): 
    if root.right != None:
        return getMin(root.right)
    y = root.parent
    while y != None and root != y.left:
        root = y
        y = y.parent
    return y

def remove(root,key):
    z = find(root,key)
    if z == None:
        return False
    else:
        if z.right == None:
            if z.left == None:
                #jeśli element nie ma dzieci po prostu go usuwamy
                if z == z.parent.left:
                    z.parent.left = None
                else:
                    z.parent.right = None
            else:
                #ma tylko lewe dziecko wtedy parent z otrzymuje dowiązanie do dziecka
                if z == z.parent.left:
                    z.parent.left = z.left
                else:
                    z.parent.right = z.left

            z = z.parent
            while z != None:
                z.idx -= 1
                z = z.parent

        elif z.left == None:
            #ma tylko prawe dziecko - analogicznie dowiązujemy do rodzica z
            if z == z.parent.right:
                z.parent.right = z.right
            else:
                z.parent.left = z.right

            z = z.parent
            while z != None:
                z.idx -= 1
                z = z.parent

        else:
            #ma i prawe i lewe dziecko wtedy następnik wskakuje na jego miejsce
            y = getNext(z)
            z.key = y.key
            # z.idx -= 1

            x = y.parent
            while x != None:
                x.idx -= 1
                x = x.parent

            if y.right == None:#jeśli nie ma żadnych dzieci
                if y == y.parent.left:
                    y.parent.left = None
                else:
                    y.parent.right = None
            else:#jeśli ma dzicko po prawej
                if y == y.parent.left:
                    y.parent.left, y.right.parent = y.right, y.parent.left
                else:
                    y.parent.right, y.right.parent = y.right, y.parent.right
            
        return True

def getSumOfSubTree(root):
    _sum = 0
    x = getMin(root)
    while x != None:
        _sum += x.key
        tmp = getNext(x)
        if root.parent == tmp:
            return _sum
        x = tmp
    return _sum

def whichInOrderIsThisNode(root,node,i=1):
    if root.left == None:
            leftSide = 0
    else:
        leftSide = root.left.idx

    if node.key == root.key:
        return leftSide + i

    if node.key < root.key:
        return whichInOrderIsThisNode(root.left,node,i)
    
    if node.key > root.key:
        return whichInOrderIsThisNode(root.right,node,i+leftSide+1)

def build(A,root,l,mid,r,n):
    #nie działa idx
    leftMid = (l+mid)//2
    rightMid = (mid+r)//2
    if leftMid < mid and (leftMid > l or leftMid == 0):
        root.left = BSTNode(A[leftMid])
        root.left.parent = root
        build(A,root.left,l,leftMid,mid,n)

    if rightMid > mid and (rightMid < r or rightMid == n-1):
        root.right = BSTNode(A[rightMid])
        root.right.parent = root
        build(A,root.right,mid,rightMid,r,n)
        

def buildTree(elements):
    elements.sort()
    n = len(elements)
    root = BSTNode(elements[(n-1)//2])
    build(elements,root,0,(n-1)//2,n,n)
    return root

# def tree_build(A, i, j, left, right):
#     X = Node()
#     X.left  = left
#     X.right = right
#     if (j < i):
#         # build leaf
#         X.cut  = -1
#         X.leaf = True
#     else:
#         # build internal node
#         m = (i + j) // 2
#         X.cut = A[m]
#         X.lchild = tree_build(A, i, m - 1, left, A[m])
#         X.rchild = tree_build(A, m + 1, j, A[m], right)
#     return X
if __name__ == "__main__":

    # I
    
    # root = BSTNode(7)
    # insert(root,3)
    # insert(root,20)
    # insert(root,1)
    # insert(root,6)
    # insert(root,18)
    # insert(root,21)
    # insert(root,23)
    # # inorderTreeWalk(root)
    # print(getSth(root,find(root,1)))
    # print(getSth(root,find(root,3)))
    # print(getSth(root,find(root,6)))
    # print(getSth(root,find(root,7)))
    # print(getSth(root,find(root,18)))
    # print(getSth(root,find(root,20)))
    # print(getSth(root,find(root,21)))
    # print(getSth(root,find(root,23)))
    # print("__________________")
    # n = 8
    # for i in range(1,n):
    #     print(getKthSmallestElement(root,i))

    # _____________________________________________
    # II

    # root = BSTNode(7)
    # insert(root,20)
    # insert(root,18)
    # insert(root,23)
    # insert(root,17)
    # insert(root,19)
    # insert(root,24)

    # print(getSth(root,find(root,7)))
    # print(getSth(root,find(root,17)))
    # print(getSth(root,find(root,18)))
    # print(getSth(root,find(root,19)))
    # print(getSth(root,find(root,20)))
    # print(getSth(root,find(root,23)))
    # print(getSth(root,find(root,24)))
    # remove(root,20)

    # inorderTreeWalk(root)
    # print("__________________")
    # n = 7
    # for i in range(1,n):
    #     print(getKthSmallestElement(root,i))
    A = [1,2,3,4,5,6,7,8,9,10]
    root = buildTree(A)
    inorderTreeWalk(root)