# # Dynamic Programming Python implementation of Matrix
# # Chain Multiplication. See the Cormen book for details
# # of the following algorithm
# import sys

# def MatrixChainOrder(p, n):
#     # For simplicity of the program,
#     # one extra row and one
#     # extra column are allocated in m[][]. 
#     # 0th row and 0th
#     # column of m[][] are not used
#     m = [[0 for x in range(n)] for x in range(n)]
 
#     # m[i, j] = Minimum number of scalar
#     # multiplications needed
#     # to compute the matrix A[i]A[i + 1]...A[j] =
#     # A[i..j] where
#     # dimension of A[i] is p[i-1] x p[i]
 
#     # cost is zero when multiplying one matrix.
#     for i in range(1, n):
#         m[i][i] = 0
 
#     # L is chain length.
#     for L in range(2, n):
#         for i in range(1, n-L + 1):
#             j = i + L-1
#             m[i][j] = sys.maxsize
#             for k in range(i, j):
 
#                 # q = cost / scalar multiplications
#                 q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
#                 if q < m[i][j]:
#                     m[i][j] = q
 
#     return m[1][n-1]
 
 
# # Driver code
# arr = [1, 2, 3, 4]
# size = len(arr)
# print("Minimum number of multiplications is " + str(MatrixChainOrder(arr, size)))
# # This Code is contributed by Bhavya Jain

def matrix_product(p):
    length = len(p)
    m = [[-1]*length for _ in range(length)]
    s = [[-1]*length for _ in range(length)]
    matrix_product_helper(p, 1, length - 1, m, s)
    return m, s

def matrix_product_helper(p, start, end, m, s):
    if m[start][end] >= 0:
        return m[start][end]
 
    if start == end:
        q = 0
    else:
        q = float('inf')
        for k in range(start, end):
            temp = matrix_product_helper(p, start, k, m, s) \
                   + matrix_product_helper(p, k + 1, end, m, s) \
                   + p[start - 1]*p[k]*p[end]
            if q > temp:
                q = temp
                s[start][end] = k
    m[start][end] = q
    return q
 
 
def print_parenthesization(s, start, end):
    if start == end:
        print('A[{}]'.format(start), end='')
        return
    k = s[start][end]
    print('(', end='')
    print_parenthesization(s, start, k)
    print_parenthesization(s, k + 1, end)
    print(')', end='')