import timeit

def gcd(lst):
    numbers = [i[0] for i in lst]
    numbers.append(lst[0][1])
    numbers = set(numbers)

    stop = False

    while not stop:
        numbers = sorted(numbers)
        x = numbers[0]
        for i, n in enumerate(numbers):
            if len(set(numbers)) == 1:
                stop = True
                break

            while x < n:
                n -= x
        
            numbers[i] = n

    return numbers[0]

def convert_fracts(lst: list):
    if lst == []: return []

    denList = [ i[1] for i in lst]
    for i in denList:
        for j in denList:
            if i == j: continue
            if i % j == 0: denList.remove(j)

    den = 1
    for i in denList:
        den*=i

    for i in lst:
        i[0] *= den // i[1]
        i[1] = den

    div = gcd(lst)

    return list(map(lambda item: list(map(lambda item2: item2 // div, item)), lst))

print(f"Tempo de execução: {timeit.timeit(lambda: print(convert_fracts([[77033412951888085, 14949283383840499], [117787497858828, 14949283383840499], [2526695441399712, 14949283383840499]])), number=1)} segundos")
# print(convert_fracts([[2,16],[0, 2],[0, 3],[0, 4],[0, 5],[0, 2],[0, 1],[2,8]]))

# print([[6, 12], [4, 12], [3, 12]])
# print(f"Tempo de execução: {timeit.timeit(lambda: print(convert_fracts([[1, 2], [1, 3], [1, 4]])), number=1)} segundos")