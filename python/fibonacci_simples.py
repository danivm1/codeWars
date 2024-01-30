import timeit
import sys

def f(n):
    if n == 0: return 0
    if n == 1: return 1

    last = [0, 0]
    r = 1

    for _ in range(1, n):
        last[1] = r
        r += last[0]
        last[0] = last[1]
    
    return r


sys.set_int_max_str_digits(500000)

print(f"Tempo de execução: {timeit.timeit(lambda: print(f(int(20))), number=1)} segundos")