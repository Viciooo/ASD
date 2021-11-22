#Zakładam że na wejściu nie dostanę root = None, i użytkownik sam stworzy BSTNode o pierwszym kluczu
#Robię tak gdyż założenia zadania nakazują, aby zwracane były jedynie wartości logiczne a nie root
#Tak samo zwracając jedynie wartości logiczne nie jestem w stanie usunąć samego roota jeśli nie ma on dzieci

#Usunięcie roota lub wstawienie go gdy na wejściu otrzymujemy root = val
#byłoby łatwe w realizacji gdyby funkcje insert i remove przyjmowały na wejściu T jako drzewo
# class BSTtree:
#     def __init__(self,root):
#         self.root = root

#zł obliczeniowa O(h) gdzie h to wysokość drzewa, jeśli jest zbalansowane to O(logn) gdzie n to ilość elementów - jeśli nie to O(n)
#zł pamięciowa O(n)


class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

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

def getMin(root):
    while root.left != None:
        root = root.left
    return root

def getMax(root):
    while root.left != None:
        root = root.left
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
        elif z.left == None:
            #ma tylko prawe dziecko - analogicznie dowiązujemy do rodzica z
            if z == z.parent.right:
                z.parent.right = z.right
            else:
                z.parent.left = z.right
        else:
            #ma i prawe i lewe dziecko wtedy następnik wskakuje na jego miejsce
            y = getNext(z)
            z.key = y.key
            if y == y.parent.left:
                y.parent.left = None
            else:
                y.parent.right = None
        
        return True
        