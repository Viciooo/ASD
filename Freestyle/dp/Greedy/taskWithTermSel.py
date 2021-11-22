# Zadanie 2. (wybór zadan z terminami) Mamy dany zbiór zadan T = {t1, . . . , tn}. Kazde zadanie ti
# dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w terminie
# (liczba naturalna). Wykonanie kazdego zadania trwa jednostke czasu. Jesli zadanie ti zostanie wykonane
# przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrode g(ti) (pierwsze wybrane zadanie
# jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Prosze podac algorytm, który znajduje podzbiór zadan, które mozna wykonac w terminie i który prowadzi
# do maksymalnego zysku. Prosze uzasadnic poprawnosc algorytmu.

def selectTaks(D,G):
    n = len(D)
    new = [(D[i],G[i]) for i in range(n)]
    new.sort(key=lambda x: x[0])
    new.sort(key=lambda x: x[1])
    cnt = max(D)+1
    solution = [None]*cnt
    i = n-1
    print(new)
    while cnt > 0:
        if solution[new[i][0]] == None:
            solution[new[i][0]] = new[i]
        else:
            for j in range(new[i][0]-1,-1,-1):
                if solution[j] == None:
                    solution[j] = new[i]
                    break
        i -= 1
        cnt -= 1
    return solution

D = [0,2,1,3,1,2]
G = [2,6,1,3,4,3]
print(selectTaks(D,G))

