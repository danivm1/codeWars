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

print(f"Tempo de execução: {timeit.timeit(lambda: dbl_linear(1000000), number=1)} segundos")


 # in u, then y = 2 * x + 1 and z = 3 * x + 1 mus
# [1, 3, 4, 7, 9, 10, 13, 15, 21, 22, 31]
# [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, 28, 31, 40, 43, 45, 46, 63, 64, 67, 94]