import time
import sys

def f(n):
    if n == 0: return 0
    if n == 1: return 1

        
    last = [0, 0]
    r = 1

    for _ in range(1, n):
        last[1] = r
        r += last[0]
        last[0] = last[1]
    
    return r

t0 = time.time()


sys.set_int_max_str_digits(500000)

result = f(int(2000000))
print(result)

t1 = time.time()

print(t1-t0)