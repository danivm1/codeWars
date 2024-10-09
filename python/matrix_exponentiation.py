# https://www.codewars.com/kata/5791bdba3467db61ff000040
from time import time
from sys import set_int_max_str_digits


def identity(l):
    mat = [[0] * l for _ in range(l)]
    for i in range(l):
        mat[i][i] = 1
    
    return mat

def bin_decomp(x):
    s = -1
    while x:
        x //= 2
        s += 1
    
    return s

def multiply(A, mat):
    l = len(A)
    B = [m[:] for m in mat]
    for i in range(l):
        for j in range(l):
            sum = 0
            for x in range(l):
                sum += B[i][x] * A[x][j]
            mat[i][j] = sum
            
    return mat

def loop(l, a):
    b = 1
    for _ in range(l):
        if l == 1: break
        a_copy = [x[:] for x in a]
        a = multiply(a, a_copy)
        b *= 2

    return a, b

def calc(A, n):
    order = len(A)
    
    if order == 0 or order > 0 and len(A[0]) != order: raise
    if n == 1: return A
    if n == 0: return identity(order)
    
    A_mult = []
    
    while n:
        l = bin_decomp(n)
        x, b = loop(l, A)
        
        A_mult.append(x)
        
        n -= b
    
    result = identity(order)
    for a in A_mult:
        result = multiply(a, result)
    
    return result


set_int_max_str_digits(10000000) 
ini = time()
# A = [[1, 2], [3, 4]]
# print(calc(A, 3))
# print(calc([[1, 2], [0, 1]], 3))
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
# A = [[1,2],[1,0]]
calc(A, 100)
print(time()-ini)