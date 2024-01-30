# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python

import timeit

def check(x, sum_dig):
    lst = [int(i) for i in str(x)]

    s = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]: return False

        s += lst[i]

    if s != sum_dig: return False

    return True


def find_all(sum_dig, digs):
    x = int("1" * digs)
    div = x
    lst = []
    b = 0

    if sum_dig > digs * 9: return []

    while x // div * digs <= sum_dig:
        if x == 208:
            pass
        a = x
        last = a%10
        s = 0
        chk = True
        index = 0
        while a != 0:
            a, b = divmod(a, 10)
            if last < b:
                chk = False
                break
            last = b
            index += 1
            s += b

        if chk and s == sum_dig:
            lst.append(x)
            print(f"Atual: {x}\t\tLen: {len(lst)}")
            x += 9
            continue

        if not chk:
            digS = str(x)[:-index]
            digS = digS + str(digS[-1]*index)
            x = int(digS)
            continue

        x += 1

    return lst
    # return [len(lst), min(lst), max(lst)] if lst else lst
    

print(timeit.timeit(lambda: print(*find_all(20, 17), sep="\n"), number=1))