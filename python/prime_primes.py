# https://www.codewars.com/kata/57ba58d68dcd97e98c00012b/train/python

import timeit

def get_primes(m: int):
    primeList = [i for i in range(3, m + 1, 2)]

    for i in primeList:
        if i > (m**0.5)//1: break

        for x in range(i*3, max(primeList) + 1, i*2):
            try: primeList.remove(x)
            except: pass

    return ([2] if m >= 2 else []) + primeList


def prime_primes(N):
    primeLst = get_primes(N)

    lst = []

    for i in primeLst:
        for j in primeLst:
            if i < j:
                lst.append(i/j)

    intPart = int(sum(lst) // 1)

    return len(lst), intPart




print(timeit.timeit(lambda: print(*prime_primes(42), sep="\n"), number=1))