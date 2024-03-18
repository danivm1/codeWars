# https://www.codewars.com/kata/5672682212c8ecf83e000050

import timeit

def dbl_linear(n):
    u = [1]
    j, k = 0, 0
    
    for i in range(1, n+1):
      y = 2 * u[j] + 1
      z = 3 * u[k] + 1

      u.append(min(y, z))
      
      if(u[i] == y): j+=1
      if(u[i] == z): k+=1

    return u

print(f"Tempo de execução: {timeit.timeit(lambda: print(dbl_linear(30), end='; '), number=1)} segundos")


 # y = 2 * x + 1 and z = 3 * x + 1 (x == last added to u)
# y = [1, 3, 7, 9, 15, 19, 21, 27, 31]
# z = [1, 4, 10, 13, 22, 28]
# u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, 28, 31]