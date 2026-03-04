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
        if n > middle: left = l+1; continue

    return -1, iterations

def naive_search(lst: list[int], n: int) -> int:
    iterations = 0
    
    for index, i in enumerate(lst):
        iterations += 1
        if n==i: return index, iterations
    return -1, iterations


lst = [i for i in range(8)]
n = 8

try:
    print(f"Binary - Execução: {__import__('timeit').timeit(lambda: print(binary_search(lst, n)), number=1)} segundos")
    print(f"Naive - Execução: {__import__('timeit').timeit(lambda: print(naive_search(lst, n)), number=1)} segundos")
except Exception as err:
    print(f"Erro: {err}")