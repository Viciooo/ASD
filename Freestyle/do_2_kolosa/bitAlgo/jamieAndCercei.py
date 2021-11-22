def nachodzo(new,i):
    if (new[i][0] > new[i-1][0] and new[i][0] < new[i-1][1] ) or (new[i][1] > new[i-1][0] and new[i][1] < new[i-1][1]):
        return True
    if (new[i-1][0] > new[i][0] and new[i-1][0] < new[i][1]) or (new[i-1][1] > new[i][0] and new[i-1][1] < new[i][1]):
        return True
    return False

def solve(A):
    n = len(A)
    new = [None for _ in range(n)]
    for i in range(n):
        new[i] = (A[i][0],A[i][1],i)
    new.sort(key=lambda x: x[1])
    letters = [None for _ in range(n)]
    solution = [None for _ in range(n)]
    flag = False
    letters[0] = 1
    solution[new[0][2]] = 'J'
    for i in range(1,n):
        if nachodzo(new,i):
            letters[i] = letters[i-1]*(-1)
            if i-2 >= 0 and flag == True and new[i-2][1] > new[i][0]:
                return "IMPOSSIBLE"
            flag = True
        else:
            letters[i] = letters[i-1]
            flag = False
        solution[new[i][2]] = 'C' if letters[i] == -1 else 'J'
    return solution


A = [(99, 150),(1, 100), (100, 301), (2,5), (150, 250)] #['J', 'C', 'C', 'J', 'J']
B = [(99,100),(1,101),(98,150)] #"IMPOSSIBLE"
print(solve(B))