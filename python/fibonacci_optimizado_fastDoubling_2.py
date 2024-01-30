import timeit
import sys

def fib(n):
    if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
    a = b = x = 1
    c = y = 0
    while n:
      if n % 2 == 0:
          (a, b, c) = (a * a + b * b,
                       a * b + b * c,
                       b * b + c * c)
          n /= 2
      else:
          (x, y) = (a * x + b * y,
                    b * x + c * y)
          n -= 1
    return y


sys.set_int_max_str_digits(500000)

print(f"Tempo de execução: { timeit.timeit(lambda: print(fib(-200)), number=1) } segundos")