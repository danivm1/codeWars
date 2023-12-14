# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python

import timeit

def prime_factors(n: int):
    p, i = 2, 1

    while p**2 <= n:
        while n % p == 0:
            yield p
            n //= p
    
        p += i
        i = 2
    
    if n > 1 : yield n


def sum_for_list(lst: list):
    d = {}

    for i in lst:
        factors = set(prime_factors(abs(i)))
        
        for j in factors:
            if not j in d.keys() : d[j] = []
            d[j].append(i)

    return [[k, sum(v)] for k, v in sorted(d.items())]




print([[2, -61548], [3, -4209], [5, -28265], [23, -4209], [31, -31744], [53, -72769], [61, -4209], [1373, -72769], [5653, -28265], [7451, -29804]])
print(f"Tempo de execução: {timeit.timeit(lambda: print(sum_for_list([-29804, -4209, -28265, -72769, -31744])), number=1)} segundos")