def func_1(x):
    return x(x)

def func_2(y):
    return 4

print(func_1(func_2))

# currying equivalente às funções acima
print((lambda x: x(x))(lambda y: 4))