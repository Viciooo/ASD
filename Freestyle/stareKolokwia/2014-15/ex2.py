class Node:
    def __init__(self,val,next=None):
        self.next = next
        self.val = val
    def __str__(self):
        return str(self.val) + "->" + str(self.next)

class TwoLists:
    def __init__(self):
        self.even = None
        self.odd = None
    def __str__(self):
        return str(self.even) + "\n" + str(self.odd)

def Split(first):
    new = TwoLists()
    odd_root = Node("!")
    even_root = Node("!")
    odd, even = odd_root, even_root
    while first != None:
        if first.val % 2 == 1:
            odd.next = first
            odd = odd.next
        else:
            even.next = first
            even = even.next
        
        first = first.next
    odd.next = even.next = None
    new.odd, new.even = odd_root.next, even_root.next
    return new

q = Node(5)
p = q
q.next = Node(2)
q = q.next
q.next = Node(1)
q = q.next
q.next = Node(4)
q = q.next
q.next = Node(7)
q = q.next

print(Split(p))

            