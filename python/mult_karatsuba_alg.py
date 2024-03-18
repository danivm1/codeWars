def karatsuba_multiply(x, y):
    if x < 10 and y < 10:
        return x * y
	
    str_x = str(x)
    str_y = str(y)
	
    m = max(len(str_x), len(str_y))
	
    str_x='0'*(m-len(str_x))+str_x
    str_y='0'*(m-len(str_y))+str_y
    
    m1=(m+1)//2
    m2=m//2
    
    low_x=int(str_x[m1:])
    high_x=int(str_x[:m1])
    low_y=int(str_y[m1:])
    high_y=int(str_y[:m1])
    
    z0 = karatsuba_multiply(low_x,low_y)
    z1 = karatsuba_multiply((low_x+high_x),(low_y+high_y))
    z2 = karatsuba_multiply(high_x,high_y)
    
    return z2 * 10 ** (2 * m2) + (z1 - z2 - z0) * 10 ** m2 + z0

x, y = 7652837462472, 37658263982576348563875328
print(f"Karatsuba        : {__import__('timeit').timeit(lambda: print(f'Karatsuba        : {karatsuba_multiply(x, y)}'), number=1)} segundos")
print(f"Python Karatsuba : {__import__('timeit').timeit(lambda: print(f'Python Karatsuba : {x*y}'), number=1)} segundos")