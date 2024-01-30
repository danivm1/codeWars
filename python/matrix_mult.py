def matrix_mult(a, b):
    n = len(a[0])

    c = [ ([0] * n) for i in range(n)] 

    for i in range(n):
        for j in range(n):
            for x in range(n):
                c[i][j] += a[i][x] * b[x][j]

    return c