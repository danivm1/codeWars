import timeit

lst = [2, 2, 2, 0]
# 937640, 767456, 981242
# 2, 2, 2, 0

def last_digit(lst):
    if not lst or lst == [0, 0]: return 1
    
    r = 1
    
    for n in lst[:0:-1]:
        if r < 4:
            r = pow(n, r)
            continue
        r = pow(n, r % 4 + 4)
        
    return pow(lst[0], r % 4 + 4 if r >= 4 else r, 10)

print(timeit.timeit(lambda: print(last_digit(lst)), number=1))