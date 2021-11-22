from random import randint, seed

class Node:
  def __init__(self):
    self.next = None
    self.value = None
    

def findEnd(first):
  p = first
  while p.next != None:
    p = p.next
  return p

def partition(low,high):
  pivot = high.value
  prev, p = low, low.next
  flag = True
  while p != high:
    if p.value > pivot:
      tmp = high.next
      q = p
      p, prev.next = p.next, p.next
      high.next = q
      q.next = tmp
      if flag == True:
        newHigh = q
        flag = False
    else:
      p, prev = p.next, p
  if flag:
    newHigh = high
  return high,prev,newHigh

def qsort(low, high):
  if low != high and low.next != high:   
    i,j,k = partition(low,high)
    qsort(low,j)
    qsort(i,k)

def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )
first = Node()
first.next = L
print("przed sortowaniem: L =", end=" ")
printlist(L) 
qsort(first,findEnd(L))
print("po sortowaniu    : L =", end=" ")
printlist(first.next)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

