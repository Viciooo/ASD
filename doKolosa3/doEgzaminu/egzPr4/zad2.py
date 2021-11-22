def insertionSortByOrd(arr,start,idx): 
    for i in range(start+1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= start and ord(key[idx]) < ord(arr[j][idx]) : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

def sortWordsOfDiffLen(arr,n):
    m = len(arr)
    new = [0]*m
    lgth = n
    c = [0]*lgth
    l = [0]*lgth
    for i in arr:
        c[len(i)] += 1
        l[len(i)] += 1
    for i in range(1,lgth):
        c[i] += c[i-1]
    for i in range(m-1,-1,-1):
        c[len(arr[i])] -= 1
        new[c[len(arr[i])]] = arr[i]
    start = m
    for i in range(lgth-1,0,-1):
        start -= l[i]
        if l[i] == 1 and i == lgth-1:
            continue
        insertionSortByOrd(new,start,i-1)
    return new

def stripOfAletter(word,letter):
    i = 0
    while word[i] == letter:
        i += 1
        if i == len(word):
            break
    return word[i:]

def pijany_mag(T):
    alfabet = []
    while True:
        if T[0][0] in alfabet:
            return False
        alfabet.append(T[0][0])
        T[0]= stripOfAletter(T[0],T[0][0])
        i = 1
        while T[i][0] == alfabet[-1]:
            T[i]= stripOfAletter(T[i],alfabet[-1])
            i += 1
        for i in T:
            if i == "":
                T.remove(i)
        cnt = 0
        for i in T:
            cnt += len(i)
        print(T,cnt,alfabet)
        if cnt == 0:
            return alfabet
    
T1= ["wrt","wrf","er","ett","rftt"]
odp1 = 'wertf'
print(pijany_mag(T1))
T2 = ['z','x']
odp2 = 'zx'

T3 = ['z','x','z']
odp3 = ''

# tests = [(T1,odp1),(T2,odp2),(T3,odp3)]
# for ind,(t,odp) in enumerate(tests):
#     print('---------')
#     print("test nr",ind)
#     print("odpowiedz:",odp)
#     a = pijany_mag(t)
#     if a != odp:
#         print(f"twoja odpowiedz: \"%s\"" % a)
#         print("Błd w tescie")
#     else:
#         print("OK")
