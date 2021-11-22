#zł czasowa O(n) gdzie n to długość słów(jeśli długości są różne to O(1) :) )
#zł pamięciowa O(n) - zakładam, że nie mogę niszczyć oryginalnej struktury

#główna idea - używam counting sorta aby posortować słowa z przypisanymi do niego numerami (na początku od 1 do n), tak posortowane STABILNIE słowo
#zapewni nam informację których potrzebujemy (counting sort jest stabilny więc nie mamy problemu)

def countSortWords(arr):
    letters = [0]*26
    n = len(arr)
    new = [0]*n
    for i in range(n):
        l = ord(arr[i][0]) - ord('a')
        letters[l] += 1
    for i in range(1,26):
        letters[i] += letters[i-1]
    for i in range(n-1,-1,-1):
        l = ord(arr[i][0]) - ord('a')
        letters[l] -= 1
        new[letters[l]] = arr[i]
    for i in range(n):
        arr[i] = new[i]

def tanagram(x, y, t):
    n = len(x)
    if len(y) != n:
        return False
    word1 = [[None,i] for i in range(n)]
    word2 = [[None,i] for i in range(n)]
    for i in range(n):
        word1[i][0] = x[i]
        word2[i][0] = y[i]
    countSortWords(word1)
    countSortWords(word2)
    for i in range(n):
        if word1[i][0] != word2[i][0] or abs(word1[i][1] - word2[i][1]) > t:
            return False
    return True

x1 = "egzamin"
y1 = "gezmina"
r1 = 3

x2 = "kotomysz"
y2 = "tokmysoz"
r2 = 3

x3 = "abaabababaaaababaaaaabaabba"
y3 = "baaaababbaaaaabbaaaabaabaab"
r3 = 1

x4 = "algorytm"
y4 = "logarytm"
r4 = 3

x5 = "sloniatko"
y5 = "oktainols"
r5 = 8

x6 = "darjeeling"
y6 = "darjeeling"
r6 = 0

TESTS = [(x1,y1,r1),
         (x2,y2,r2),
         (x3,y3,r3),
         (x4,y4,r4),
         (x5,y5,r5),
         (x6,y6,r6)]
         

def runtests( f ):
  OK = True
  print("hi")
  for x,y,r in TESTS:
    print("--------")
    print("x = ", x)
    print("y = ", y)
    for t in range(len(x)):
      RESULT = f(x,y,t)

      if RESULT != (t >= r):
        OK = False
        print("t = ", t)     
        print("oczekiwana odpowiedź: ", t >= r )
        print("uzyskana   odpowiedź: ", RESULT )
        print("Problem!")
        
  if OK: print("OK!")
  else : print("Problemy!")

runtests(tanagram)