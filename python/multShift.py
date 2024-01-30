import timeit

def multShift(x, y):
    r = 0
    while y > 0:
        if y & 1:
            r += x
        x <<= 1
        y >>= 1
    return r


a = 1243
b = 53728
print(f"Tempo de execução: {timeit.timeit(lambda: multShift(a, b), number=1)} segundos")
print(f"Tempo de execução: {timeit.timeit(lambda: a * b, number=1)} segundos")