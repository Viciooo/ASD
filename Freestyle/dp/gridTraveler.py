#Na ile sposobów możesz przemieścić się z lewego górnego rogu do prawego dolnego rogu jeśli
#można poruszać się tylko w dół lub w prawo

def bfSolution(m,n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return bfSolution(m-1,n)+bfSolution(m,n-1)

def dpSolution(m,n,memo={}):
    key = (m,n)
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1 
    memo[key] = dpSolution(m-1,n,memo)+dpSolution(m,n-1,memo)
    return memo[key]

print(dpSolution(18,18))
