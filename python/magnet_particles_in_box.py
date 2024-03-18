# https://www.codewars.com/kata/56c04261c3fcf33f2d000534

import numpy as np

def doubles(maxk, maxn):
    total_force = 0
    for k in range(1, maxk+1):
        total_force += np.sum(1 / (k * np.arange(2, maxn+2, dtype=np.float64) ** (2 * k)))
    return total_force

k, n = 10, 1000
print(f"Execução: {__import__('timeit').timeit(lambda: print(doubles(k, n)), number=1)} segundos")

# v(k, n) = 1/(k*(n+1)**(2*k))
# u(1, N) = (1/(k*(1+1)**(2*k))) + (1/(k*(2+1)**(2*k))) + ... + (1/(k*(N+1)**(2*k)))

# S(K, N) = (1/(1*(1+1)**(2*1))) + (1/(1*(2+1)**(2*1))) + ... + (1/(1*(N+1)**(2*1)))
#         + (1/(2*(1+1)**(2*2))) + (1/(2*(2+1)**(2*2))) + ... + (1/(2*(N+1)**(2*2)))
#         +       ...           +       ...           + ... +       ...
#         + (1/(K*(1+1)**(2*K))) + (1/(K*(2+1)**(2*K))) + ... + (1/(K*(N+1)**(2*K)))
