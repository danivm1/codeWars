def matrix_addition(a, b):
    n = len(a[0])
    c = [ ([0] * n) for _ in range(n) ]
    
    for i in range(n): 
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]

    return c

print(matrix_addition(
                       [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
#       +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] ))