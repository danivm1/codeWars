# https://www.codewars.com/kata/5791bdba3467db61ff000040

# recursive
# def calc(A, n, B=None):
#     l = len(A)
    
#     if l > 0 and len(A[0]) != l: raise
    
#     if B == None: B = A
    
#     mat = [[0] * l for _ in range(l)]
    
#     for i in range(l):
#         for j in range(l):
#             sum = 0
#             for x in range(l):
#                 sum += B[i][x] * A[x][j]
#             mat[i][j] = sum
            
#     n -= 1
      
#     return mat if n == 1 else calc(A, n, mat)

def identity(l):
    mat = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            mat[i][j] = 1 if i == j else 0
    
    return mat

def multiply(A, mat, l):
    B = [m[:] for m in mat]
    for i in range(l):
        for j in range(l):
            sum = 0
            for x in range(l):
                sum += B[i][x] * A[x][j]
            mat[i][j] = sum
            
    return mat

def calc(A, n):
    l = len(A)
    
    if l == 0 or l > 0 and len(A[0]) != l: raise
    if n == 1: return A
    if n == 0: return identity(l)
    
    mat = [a[:] for a in A]
    
    
    # (A^(n//2))^2 * (A if n%2 else 1)
    isOdd = n%2
    n //= 2
    
    while n > 1:
        mat2 = [m[:] for m in mat]
        mat = multiply(mat2, mat, l)
        n -= 1
    
    
    return multiply(A, mat, l) if isOdd else mat



# A = [[1, 2], [3, 4]]
# print(calc(A, 3))
# print(calc([[1, 2], [0, 1]], 3))

# A = [[1,2,3],[4,5,6],[7,8,9]]
A = [[1,2],[1,0]]
print(calc(A, 2))