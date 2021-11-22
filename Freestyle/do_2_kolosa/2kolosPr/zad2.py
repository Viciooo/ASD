from queue import Queue

#Pomysł tworzę sobie kolejkę dodając do niej elementy które zaczynają się tam gdzie zaczyna się prz(!XD)
#zdejmuje odc z kolejki i dlatego że posortowałem tablicę mogę szukać w niej binsearchem początku takiego że pasuje do końca przerabianego odc 
#i jednocześnie koniec tamtego odc nie wystaje poza prz. Oczywiście spamiętuje sumę ceny i sklejam wszystkie pasujące kawałki.
#Jak przedział będzie == prz to biorę min z jego ceny i ceny najniższej do tej pory
#kończę jak wyczerpie się kolejka
#zł czasowa: O(nlogn)
#zł pamięciowa O(n)
def binSearch(arr,val):
    n = len(arr)
    low, high, mid = 0, n-1, (n-1)//2
    while low <= high:
        if val < arr[mid][0]:
            high = mid-1
            mid = (low+high)//2
        elif val > arr[mid][0]:
            low = mid+1
            mid = (low+high)//2
        else:
            return mid
    return -1

def kopula(P,prz):
    P.sort()
    n = len(P)
    q = Queue()
    i = 0
    cost = float("inf")
    while i < n and P[i][1] <= prz[1]:
        if P[i][0] == prz[0]:
            q.put(P[i])
        i += 1
    while not q.empty():
        tmp = q.get()
        pos = binSearch(P,tmp[1])
        if pos == -1:
            if tmp[0] == prz[0] and tmp[1] == prz[1]:
                cost = min(cost,tmp[2])
            continue
        else:
            j = pos
            while j >= 0 and P[j][0] == P[pos][0]:
                j -= 1
            j += 1
            while j < n and P[j][0] == P[pos][0] and P[j][1]<=prz[1]:
                if P[j][1]<=prz[1]:
                    q.put((tmp[0],P[j][1],tmp[2]+P[j][2]))
                j += 1
    return cost if cost != float("inf") else -1


P1 = [(1,2,10),(2,5,2),(1,5,20)]
odp1 = 12
prz1 = (1,5)

P2 = [(1,3,20),(2.8,4,50),(7,50,2),(1250,1251,1)]
odp2 = -1
prz2 = 2.8,3

P3 = [(1,3,20),(2.8,4,50),(7,50,2),(1250,1251,1)]
odp3 = -1
prz3 = 1,1251

P4 = [(1,3,20),(2.8,4,50),(7,50,2),(1250,1251,1),(3,7,2),(7,10,12),(1,10,36)]
odp4 = 34
prz4 = 1,10

P5 = [(1,3,20),(2.8,4,50),(7,50,2),(1250,1251,1)]
odp5 = -1
prz5 = 1,4

P = [P1,P2,P3,P4,P5]
odp = [odp1,odp2,odp3,odp4,odp5]
prz = [prz1,prz2,prz3,prz4,prz5]

def runtests(ez):
    git = True
    for i in range(len(P)):
        print(P[i])
        ret = ez(P[i],prz[i])
        print("otrzymany wynik:" + str(ret))
        print("oczekiwany wynik:" + str(odp[i]))
        print("git" if ret == odp[i] else "Błąd mordo zmien cos")
        if ret != odp[i]:
            git = False
        print("-----------------------------------")
    if not git:
        print("wynik:   tiny.cc/pudzian")
    else:
        print("wynik:   tiny.cc/pudzianv2")

runtests(kopula)
