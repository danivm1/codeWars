def binary_search(lst: list[int], n: int) -> int:
    if lst != sorted(lst): raise Exception("Lista não ordenada")
    
    left = 0
    right = len(lst)

    while left < right:
        l = left + ((right - left) // 2)
        middle = lst[l]

        if n == middle: return l
        if n < middle: right = l; continue
        if n > middle: left = l; continue
        if not l: break

    return -1


lst = [i for i in range(1000000)]
n = 999999

try:
    print(f"Execução: {__import__('timeit').timeit(lambda: print(binary_search(lst, n)), number=1)} segundos")
except Exception as err:
    print(f"Erro: {err}")