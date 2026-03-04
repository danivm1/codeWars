def green(n):
    a = []
    i = 1
    while len(a) < n:
        if i**2%10**len(str(i)) == i:
            a.append(i)
        i += 1
            
    return a

import timeit
print(timeit.timeit(lambda: green(12), number=1))