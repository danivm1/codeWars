import time
import sys

def fibonacci(n):
    if n < 0: n *= -1
    
    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2:
            return (d, c + d)
        else:
            return (c, d)


def fib(n):
    isNeg = n < 0
    
    f = fibonacci(n)[0]
    
    return f * -1 if (isNeg and not n % 2) else f
        

t0 = time.time()

sys.set_int_max_str_digits(500000)

print(fib(-2000000))

t1 = time.time()

print(t1-t0)