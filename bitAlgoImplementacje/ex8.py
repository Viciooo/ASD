# Dana jest klasa :
# class Node:
# 	val = 0
# 	next = None
# reprezentująca węzeł jednokierunkowego łańcucha odsyłaczowego,
# w którym wartości val poszczególnych węzłów zostały wygenerowane 
# zgodnie z rozkładem jednostajnym na przedziale [a, b].
# Napisz procedurę sort(first), która sortuje taką listę. Funkcja powinna być jak najszybsza. 

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value) + "->" + str(self.next)

def tab_to_lista(tab):
    head = Node("!")
    last = head
    for i in tab:
        last.next = Node(i)
        last = last.next
    return head.next

def selectionSort(head): 
    temp = head 
    while (temp): 
        minn = temp 
        r = temp.next          
        while (r): 
            if (minn.value > r.value): 
                minn = r 
            r = r.next
        x = temp.value 
        temp.value = minn.value 
        minn.value = x 
        temp = temp.next

def sortList(first):
    p = first.next
    a = b = first.value
    n = 0
    while p.next != None:
        if p.value < a:
            a = p.value
        elif p.value > b:
            b = p.value
        p = p.next
        n += 1
    buckets = [Node("!") for _ in range(n)]
    lasts = [buckets[i] for i in range(n)]
    p = first
    while p != None:
        norm_num = p.value / b
        bucketIdx = int(n * norm_num - 0.001) #po to aby na pewno największy el zmieścił się w tablicy
        lasts[bucketIdx].next = p
        lasts[bucketIdx] = lasts[bucketIdx].next
        p = p.next
    for i in range(n):
        buckets[i] = buckets[i].next
        lasts[i].next = None
        selectionSort(buckets[i])
    new = Node("!")
    p = new
    for i in range(n):
        p.next = buckets[i]
        while p.next != None:
            p = p.next
    return new.next

arr = [1,7,4,5,1,3,2]
first = tab_to_lista(arr)
# print(first)
first = sortList(first)
print(first)

    
    
