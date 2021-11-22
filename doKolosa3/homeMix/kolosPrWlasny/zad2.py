class Cyclist:
    def __init__(self,id,n_id): # prosze nie usuwac tej funkcji(uzywaja ja testy w takiej formie jak jest)
        self.id = id
        self.n_id = n_id

#robię listę liderów groups dla każdego lidera czyli groups[i] w grouplen[i] przechowywana jest liczba kolarzy w tej grupie 
#binsearchem szukam poprzedniego kolarza w grupie tego co wcześniej był liderem rzucam dzikim zwierzętom na pożarcie i obecnego daję na lidera 
#licznik spamięta pożartych liderów i obecnego min z tej tablicy to wynik
#nie robię na linkedListach bo jest pi.atek i mi się nie chce a one są zbędne
#zł obliczeniowa O(nlogn)
#zł pamięciowa O(k) - k to liczba liderów
def binSearch(arr,val):
    n = len(arr)
    low, high, mid = 0, n-1, (n-1)//2
    while low <= high:
        if val < arr[mid][1]:
            high = mid-1
            mid = (low+high)//2
        elif val > arr[mid][1]:
            low = mid+1
            mid = (low+high)//2
        else:
            return arr[mid][0]
    return -1

def smallestGroup(cyclist_list, n):
    cyclist_list.sort(key=lambda x: x[1])
    groups = []
    groupLen = []
    for i,j in cyclist_list:
        if j == -1:
            groups.append(i)
            groupLen.append(1)
    m = len(groups)
    for i in range(m):
        while True:
            idx = binSearch(cyclist_list,groups[i])
            if idx == -1:
                break
            groups[i] = idx
            groupLen[i] += 1
    return min(groupLen) if len(groupLen) > 0 else 0

G1 = [(12422,9867),(9867,-1),(888,12422),(98456757,44),(44,1),(99,6),(1,99),(6,-1)]
odp1 = 3

G2 = [(12422,9867),(9867,8),(888,12422),(98456757,44),(44,1),(99,6),(1,99),(6,-1),(8,-1)]
odp2 = 4

G3 = [(12422,9867),(9867,8),(888,12422),(98456757,44),(44,1),(99,6),(1,99),(6,-1),(8,-1),(4444688985,-1)]
odp3 = 1

G4 = []
odp4 = 0
print(smallestGroup(G4,-1))