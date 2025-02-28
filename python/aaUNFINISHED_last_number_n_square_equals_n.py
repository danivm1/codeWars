# https://www.codewars.com/kata/584dee06fe9c9aef810001e8/train/python



# Testar lógica (n^2 - n) // 10^len(n) == 0



import timeit
import sys

sys.set_int_max_str_digits(500000)

def green(n):
    lst = [1]
    
    x = 0
    last5 = 5
    last6 = 6
    i = 0
    k = 1
    ins5 = False
    ins6 = False

    while len(lst) < n:        
        if not ins5:
            x = last5 + 10**(k-1) * i

            # if str(x**2).endswith(str(x)) and x not in lst:
            if x**2%10**len(str(x)) == x:
                lst.append(x)
                last5 = x
                ins5 = True
                # print(x)

        if not ins6:
            y = last6 + 10**(k-1) * i

            # if str(y**2).endswith(str(y)) and y not in lst:
            if y**2%10**len(str(y)) == y:
                lst.append(y)
                last6 = y
                ins6 = True
                # print(y)

        i += 1

        if i == 10 or (ins5 and ins6):
            k += 1
            i = 1
            ins5 = False
            ins6 = False

    # print('-'*20)
    # print(len(lst))
    # print('-'*20)
    return sorted(lst)


print(timeit.timeit(lambda: green(5000), number=1))



# 01 - 1
# 02 - 5
# 03 - 6
# 04 - 25
# 05 - 76
# 06 - 376
# 07 - 625
# 08 - 9376
# 09 - 90625
# 10 - 109376
# 11 - 890625
# 12 - 2890625
# 13 - 7109376
# 14 - 12890625
# 15 - 87109376
# 16 - 212890625
# 17 - 787109376
# 18 - 1787109376
# 19 - 8212890625
# 20 - 18212890625
# 21 - 81787109376
# 22 - 918212890625
# 23 - 9918212890625
# 24 - 40081787109376
# 25 - 59918212890625
# 26 - 259918212890625
# 27 - 740081787109376
# 28 - 3740081787109376
# 29 - 6259918212890625
# 30 - 43740081787109376
# 31 - 56259918212890625
# 32 - 256259918212890625
# 33 - 743740081787109376
# 34 - 2256259918212890625
# 35 - 7743740081787109376
# 36 - 92256259918212890625
# 37 - 392256259918212890625
# 38 - 607743740081787109376
# 39 - 2607743740081787109376
# 40 - 7392256259918212890625
# 41 - 22607743740081787109376
# 42 - 77392256259918212890625
# 43 - 977392256259918212890625
# 44 - 9977392256259918212890625