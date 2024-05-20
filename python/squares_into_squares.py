# https://www.codewars.com/kata/54eb33e5bc1a25440d000891

def decompose(n):
    lst = [n]
    lst2 = [n**2]
    i = n

    while lst2[-1]:
        i -= 1
        
        if not i:
            lst.pop()
            i = lst.pop()
            lst2.pop()
            lst2.pop()
            if not lst or not lst2: return None
            continue

        lst.append(i)
        lst2.append(lst2[-1] - i**2)

        x = lst2[-1]**.5//1 + 1 if i > 1 else i
        i = int(x) if x < i+1 else i

    return None if not lst else lst[:0:-1]

print(decompose(50))