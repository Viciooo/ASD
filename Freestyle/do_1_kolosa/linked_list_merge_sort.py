class Node:

  def __init__(self,val,next=None):
    self.next = None
    self.val = val

  def __str__(self):
    return str(self.val) + "->" + str(self.next)

def tab_to_lista(tab):
  head = Node("!")
  last = head
  for i in tab:
      last.next = Node(i,None)
      last = last.next
  return head.next

def getMiddle(first):
  slow = fast = first
  while fast.next != None and fast.next.next != None:
    slow = slow.next
    fast = fast.next.next
  return slow

def merge(a,b): 
  result = None
  if a == None: 
    return b 
  if b == None: 
      return a 
  if a.val <= b.val: 
      result = a 
      result.next = merge(a.next, b) 
  else: 
      result = b 
      result.next = merge(a, b.next) 
  return result 

def mergeSort(f):
  if f == None or f.next == None: 
    return f
  m = getMiddle(f) 
  nextM = m.next
  m.next = None
  l = mergeSort(f) 
  r = mergeSort(nextM) 
  sortedlist = merge(l, r) 
  return sortedlist


t = [1,2,9,11,9,1,0,11,1]

foo = tab_to_lista(t)
foo = mergeSort(foo)
print(foo)