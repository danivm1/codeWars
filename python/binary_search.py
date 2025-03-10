def binary_search(lst: list[int], n: int) -> int:
    if lst != sorted(lst): raise Exception("Lista não ordenada")
        
    left = 0
    right = len(lst)
    iterations = 0

    while left < right:
        l = left + ((right - left) // 2)
        middle = lst[l]
        iterations +=1

        if n == middle: return l, iterations
        if n < middle: right = l; continue
        if n > middle: left = l; continue
        
    return -1

def normal_search(lst: list[int], n: int) -> int:
    iterations = 0
    
    for i in lst:
        iterations += 1
        if n==i: return i, iterations
    return -1


lst = [i for i in range(1000000)]
n = 999999

try:
    print(f"Binary - Execução: {__import__('timeit').timeit(lambda: print(binary_search(lst, n)), number=1)} segundos")
    print(f"Normal - Execução: {__import__('timeit').timeit(lambda: print(normal_search(lst, n)), number=1)} segundos")
except Exception as err:
    print(f"Erro: {err}")