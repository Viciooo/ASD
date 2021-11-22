# Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę
# liczb naturalnych długości n o zakresie wartości [0, k]. 
# Ma ona posiadać metodę count_num_in_range(a, b) - ma ona zwracać informację o tym,
# ile liczb w zakresie [a, b] było w tablicy, ma działać w czasie O(1).
# Można założyć, że zawsze a >= 1, b <= k.

class Struct:
    def __init__(self):
        self.arr = [None]
        self.k = None
    def datafy(self):
        c = [0]*(self.k+1)
        for i in range(len(self.arr)):
            c[self.arr[i]] += 1
        for i in range(1,self.k+1):
            c[i] += c[i-1]
        self.values = c
    def count_num_in_range(self,a, b):
        return self.values[b] - self.values[a-1]

new = Struct()
new.arr = [1,2,7,14,3,1]
new.k = max(new.arr)
new.datafy()
print(new.k)
a = new.count_num_in_range(1,14)
print(a)