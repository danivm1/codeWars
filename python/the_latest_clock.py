# https://www.codewars.com/kata/58925dcb71f43f30cd00005f

import bisect

def bsct(lst: list, lim: int, r: bool = False):
    return bisect.bisect(lst, lim if not r else 1) - 1

def latest_clock(a, b, c, d):
    r = False
    
    while 1:
        lst = sorted([a, b, c, d])

        i = bsct(lst, 2, r)
        h1 = lst.pop(i)

        i = bsct(lst, 9 if h1 != 2 else 3)
        h2 = lst.pop(i)

        i = bsct(lst, 5)
        if i < 0:
            lst.append(h1)
            lst.append(h2)
            r = True
            continue

        m1 = lst.pop(i)

        m2 = lst[0]
        
        break

    return f"{h1}{h2}:{m1}{m2}"

print(latest_clock(1, 2, 8, 9))