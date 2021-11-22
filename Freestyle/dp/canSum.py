# def bfSolution(s,arr):
#     if s == 0:
#         return True 
#     if s < 0:
#         return False
#     for i in arr:
#         bfSolution(s-i,arr)
#         if bfSolution(s-i,arr):
#             return True
#     return False

# print(bfSolution(300,[3,4,3,7]))

def dpSolution(s,arr,memo=[]):
    if s in memo:
        return False
    if s == 0:
        return True 
    if s < 0:
        return False
    for i in arr:
        dpSolution(s-i,arr,memo)
        if dpSolution(s-i,arr,memo):
            return True
    memo.append(s)
    return False

def howSum(s,arr,memo=[],res=[]):
    if s in memo:
        return False
    if s == 0:
        return res 
    if s < 0:
        return False
    for i in arr:
        tmp = howSum(s-i,arr,memo,res+[i])
        if tmp != False:
            return tmp
    memo.append(s)
    return False
# print(howSum(300,[3,7,14]))
#czasowo O(s*(len(arr))**2)
#pamięciowo O(s*s)
best = None
def bestSum(s,arr,memo=[],res=[]):
    global best
    if s in memo:
        return 
    if s == 0:
        if best == None or len(res) < len(best):
            best = res
        return  
    if s < 0:
        return 
    for i in arr:
        bestSum(s-i,arr,memo,res+[i])
    memo.append(s)
    return 

bestSum(8,[3,5,8])
print(best)

