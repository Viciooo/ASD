# Dostajemy na wejściu trzy stringi: A, B i C. A i B są tej samej długości. Zachodzą następujące właściwości:
# Litery na tym samym indeksie w stringach A i B są równoważne
# Jeżeli litera a jest równoważna z literą b, to litera b jest równoważna z literą a
# Jeżeli litera a jest równoważna z b, a litera b z literą c, to litera a jest równoważna z literą c
# Każda litera jest równoważna sama ze sobą

# W stringu C możemy zamienić dowolną literę z literą do niej równoważną. 
# Jaki jest najmniejszy leksykograficznie string, który możemy w tej sposób skonstruować?

#zł obliczeniowa O(n^2)
#zł pamięciowa O(n+m) n to długość litery C a m to dł litery A i B

class Node:
    def __init__(self,val):
        self.val = val
        self.parent = self
    def __str__(self):
        return str(self.val)

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        if ord(x.val) < ord(y.val):
            y.parent = x
        else:
            x.parent = y

def prepareStruct(A,B):
    letters = [Node(chr(ord("a")+i)) for i in range(27)]
    n = len(A)
    for i in range(n):
        union(letters[ord(A[i])-ord("a")],letters[ord(B[i])-ord("a")])
    return letters

def solve(A,B,C):
    letters = prepareStruct(A,B)
    n = len(C)
    D = ""
    for i in range(n):
        D += find(letters[ord(C[i])-ord("a")]).val
    return D

print(solve("wbed","efca","wujda"))