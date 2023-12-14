# https://www.codewars.com/kata/5517fcb0236c8826940003c9/train/python

import timeit


def gcd(a, b):
    while b != 0:
        return gcd(b, a % b)
    return a, b


def sum_fracts(lst):
    if lst == []: return

    denList = [i[1] for i in lst]
    for i in denList:
        for j in denList:
            if i == j: continue
            if i % j == 0: denList.remove(j)

    den = 1
    for i in denList:
        den*=i

    num = 0
    for i in lst:
        i[0] *= den // i[1]
        i[1] = den
        num += i[0]
    
    if num % den == 0: return num // den

    r = gcd(num, den)[0]

    return [num // r, den // r]

print(2)
print(f"Tempo de execução: {timeit.timeit(lambda: print(sum_fracts([[1, 3], [5, 3]])), number=1)} segundos")