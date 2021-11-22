# zadanie1. Posiadając na wejściu drzewo bst znajdź największa i najmniejsza pionowa
# sumę.
# Pamięć nie jest ograniczona. Drzewo może być niezbalansowane. Wartości w drzewie są
# liczbami rzeczywistymi. Należy zwrócić krótkie (max,min). Struktura może zostać
# zmodyfikowana jeżeli argumenty konstruktora(__init__) zostaną nienaruszone (do testów)
# Rysunek z przykładem:

#Złożoność czasowa O(n) gdzie n to ilość elementów w drzewie
#Złożoność pamięciowa O(n)

#Główna idea:
#Robię tablicę leftSum dla "ujemnego indexowania" i rightsum dla "dodatniego":
#ujemne indexy to te w których sekwencja dotarcia do danej komórki składa się z większej ilości przejść do lewego dziecka niż do prawego dziecka.
#wyjątkiem jest idx zerowy w obu tablicach - odpowiada on sytuacji gdy zejśc w lewo i prawo jest po równo
#Korzystam z faktu że append ma zamortyzowany czas stały i dlatego zł czasowej nie wywali w kosmos :)

class Node:
    def __init__(self,key,left=None,right=None):
        self.key = key
        self.right = right
        self.left = left

def maxi_suma_pionowa(root):
    leftSum = [root.key]
    rightSum = [root.key]
    def travel_tree(root,curr):
        nonlocal leftSum,rightSum
        if root.left != None:
            if curr - 1 == 0:
                leftSum[0] += root.left.key
                rightSum[0] += root.left.key
                travel_tree(root.left,curr-1)

            elif curr - 1 < 0:
                while len(leftSum) <= abs(curr-1):
                    leftSum.append(0)
                leftSum[abs(curr-1)] += root.left.key
                travel_tree(root.left,curr-1)
            else:
                rightSum[curr-1] += root.left.key
                travel_tree(root.left,curr-1)

        if root.right != None:
            if curr + 1 == 0:
                leftSum[0] += root.right.key
                rightSum[0] += root.right.key
                travel_tree(root.right,curr+1)

            elif curr + 1 > 0:
                while len(rightSum) <= curr+1:
                    rightSum.append(0)
                rightSum[curr+1] += root.right.key
                travel_tree(root.right,curr+1)
            else:
                while len(leftSum) <= abs(curr+1):
                    leftSum.append(0)
                leftSum[abs(curr+1)] += root.right.key
                travel_tree(root.right,curr+1)

    travel_tree(root,0)

    return max(max(leftSum),max(rightSum)),min(min(leftSum),min(rightSum))
                    

#-1 pkt bo długie


root = Node(1)
root.left = Node(2)
root.right = Node(3,Node(5,Node(7),Node(8)),Node(6))
print(maxi_suma_pionowa(root),"?=?",11,",",6)

root = Node(-10,
        Node(-20,
            None,
            Node(-11)),
        Node(100,
            Node(90,
                Node(5,
                    None,
                    Node(50)),
                Node(95)),
            Node(105,
                Node(102),
                None)))
print(maxi_suma_pionowa(root),"?=?",195,",",-15)