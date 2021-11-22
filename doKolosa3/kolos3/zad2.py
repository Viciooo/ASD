from zad2testy import runtests
#Piotr Witek
#$Opis algorytmu:

#W zadaniu nie przewidujemy możliwości braku rozwiązania więc zakładam że koszt usunięcia liścia to float("inf") czyli operacja skrajnie nieopłacalna.
#Przy użyciu rekurencji schodzę do dzieci każdego węzła i wyznaczam koszt usunięcia tego noda. Należy uwzględnić przypadek że węzeł rozważany jest rootem drzewa
#Wtedy nie mamy wyboru i musimy wynik pobrać od obu dzieci w przeciwieństwie do innych węzłów w których rozważamy sumę wszystkich dzieci lub wartości noda

#$Złożoność czasowa: O(n) gdzie n to ilość węzłów w drzewie
#$Złożoność pamięciowa: O(n) - pamięć potrzebna na stos systemowy do rekurencji

#$Uzasadnienie poprawności: 

#Przy tak prostym algorytmie ciężko o uzasadnienie.
#Rozważamy wszystkie możliwe wybory pozbycia się nodów, dzięki rekurencji robimy to przechodząc po wszyskich nodach tylko raz
#Dzięki temu że jest to drzewo mamy czas wielomianowy a nie exponencjalny


class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

def getCost(T,root):
    if T.left == None:
        if T.right == None:
            return float("Inf")
        else:
            result = min(T.value,getCost(T.right,root))
    elif T.right == None:
        result = min(T.value,getCost(T.left,root))
    else:
        if T == root:
            result = getCost(T.left,root) + getCost(T.right,root)
        else:
            result = min(T.value,getCost(T.left,root) + getCost(T.right,root))
    return result



def cutthetree(T):
    return getCost(T,T)

runtests(cutthetree)


