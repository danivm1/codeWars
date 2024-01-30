# https://www.codewars.com/kata/56c04261c3fcf33f2d000534

# from decimal import Decimal

# def doubles(maxk, maxn):
#     s = 0.
#     for k in range(1, maxk + 1):
#         for n in range(1, maxn + 1):
#             s += 1/(k*(n+1)**(2*k))

#     return s


import numpy as np
from numpy import inf 
def doubles(maxk, maxn):
    '''Calculates the force of a box of magnets. See Magnet particules in boxes
    for more details'''
    total_force = 0
    for k in range(1, maxk+1):
        total = (1/(k*np.arange(2, maxn+2)**(2*k)))
        print(total)
        total[total == inf] = 0
        total_force += np.sum(total)
    return total_force

k, n = 90, 10000
print(f"Execução: {__import__('timeit').timeit(lambda: print(doubles(k, n)), number=1)} segundos")

# v(k, n) = 1/(k*(n+1)**(2*k))
# u(1, N) = (1/(k*(1+1)**(2*k))) + (1/(k*(2+1)**(2*k))) + ... + (1/(k*(N+1)**(2*k)))

# S(K, N) = (1/(1*(1+1)**(2*1))) + (1/(1*(2+1)**(2*1))) + ... + (1/(1*(N+1)**(2*1)))
#         + (1/(2*(1+1)**(2*2))) + (1/(2*(2+1)**(2*2))) + ... + (1/(2*(N+1)**(2*2)))
#         +       ...           +       ...           + ... +       ...
#         + (1/(K*(1+1)**(2*K))) + (1/(K*(2+1)**(2*K))) + ... + (1/(K*(N+1)**(2*K)))
