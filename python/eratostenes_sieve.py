import timeit


def yield_primes(m: int):
    primeList = [i for i in range(3, m + 1, 2)]

    if m >= 2:
        yield 2

    loopCounter = 0

    for i in primeList:
        yield i

        loopCounter += 1

        if i > (m**0.5)//1: break
        
        for x in range(i*i, max(primeList) + 1, i*2):
            try: primeList.remove(x)
            except: pass

    for i in primeList[loopCounter:]: yield i


def return_primes(m: int):
    primeList = [i for i in range(3, m + 1, 2)]

    for i in primeList:
        if i > (m**0.5)//1: break
        
        for x in range(i*i, max(primeList) + 1, i*2):
            try: primeList.remove(x)
            except: pass

    return ([2] if m >= 2 else []) + primeList



print(f"Tempo de execução: {timeit.timeit(lambda: [print(i, end=', ') for i in  yield_primes(100)], number=1)} segundos")
print(f"Tempo de execução: {timeit.timeit(lambda: [print(i, end=', ') for i in return_primes(100)], number=1)} segundos")


# return m=1000000 Tempo de execução: 2518.129956699908 segundos
# yield  m=1000000 Tempo de execução: 1991.4672632999718 segundos