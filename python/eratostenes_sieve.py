import timeit


def get_primes(m: int):
    primeList = [i for i in range(3, m + 1, 2)]

    for i in primeList:
        if i > (m**0.5)//1: break

        for x in range(i*3, max(primeList) + 1, i*2):
            try: primeList.remove(x)
            except: pass

    return ([2] if m >= 2 else []) + primeList

print(f"Tempo de execução: {timeit.timeit(lambda: print([i for i in get_primes(1000)]), number=1)} segundos")