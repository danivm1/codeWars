import timeit

def get_primes(m: int):
    primeList = [i for i in range(2, m + 1)]

    for i in primeList:
        for x in range(i*2, max(primeList) + 1, i):
            try: primeList.remove(x)
            except: pass

        if i > (m**0.5)//1: break

    return primeList

print(f"Tempo de execução: {timeit.timeit(lambda: print([i for i in get_primes(315)]), number=1)} segundos")