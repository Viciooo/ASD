class genNode:
    def __init__(self) -> None:
        self.G = None
        self.A = None
        self.T = None
        self.C = None

def insert(root,s):
    n = len(s)
    flag = False
    for i in range(n):
        if s[i] == "G":
            if root.G == None:
                flag = True
                root.G = genNode()
            root = root.G
        if s[i] == "A":
            if root.A == None:
                flag = True
                root.A = genNode()
            root = root.A
        if s[i] == "T":
            if root.T == None:
                flag = True
                root.T = genNode()
            root = root.T
        if s[i] == "C":
            if root.C == None:
                flag = True
                root.C = genNode()
            root = root.C
    return flag

def solve(arr):
    root = genNode()
    for i in arr:
        if not insert(root,i):
            return False
    return True


arr = ["GATC","GTCA","GGGGA","GATC"]
arr1 = ["GATC","GTCA","GGGGA","GATCA"]
print(solve(arr))
print(solve(arr1))
#złożoność pamięciowa O(4^k) - k to długość najdłuższej sekwencji
#zł czasowa O(n*k) - n to ilośc słów