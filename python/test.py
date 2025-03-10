def bin_decomp(x):
    s = -1
    while x:
        x //= 2
        s += 1
    
    return s
    
def loop(l, a):
    b = 1
    for _ in range(l):
        if l == 1: break
        a *= a
        b *= 2
    
    return a, b

def power(a, n):
    a_mult = []
    while n:
        l = bin_decomp(n)
        x, b = loop(l, a)
    
        a_mult.append(x)
    
        n -= b
    
    result = 1
    for i in a_mult: result *= i 
    
    return result

a = 2
l = 100
x=[]
for a in range(l):
    for n in range(l):
        x.append(bool(power(a, n) == a**n))
        # print(n)
        # print(len(power(a, n))-1)
        # print(len(str(a**n))-1)
print(all(x))

# 10^20

# 20 / 5 = 4 --> 10^2^2^2^2
# 10100

# 10^2^2^2^2

# 20 2
#  0 10 2
#     0 5 2
#       1 2 2
#         0 1
#               10100
              
              
# 10^15

# 15
# 1111

# 15 2
#  1 7 2
#    1 3 2
#      1 1
#           1111

#        10^31
# a = 10^2^2^2^2 = 10^16
# b = 10^2^2^2   = 10^8
# c = 10^2^2     = 10^4
# d = 10^2       = 10^2
# e = 10         = 10^1
# a * b * c * d * e = 10^31


# 60
# 54 
# 4
# 2
#
#
#
#
#
#
#
#
#
#
#