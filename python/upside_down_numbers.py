# https://www.codewars.com/kata/59f7597716049833200001eb/train/python

def mirror(i: int) -> bool:
    i = str(i)
    l = len(i)

    if l == 1: return True

    lst1 = [int(x) for x in i[:l//2]]
    lst2 = [int(x) for x in i[l//2:]] if not l % 2 else [int(x) for x in i[l//2+1:]]

    for x in range(len(lst2)):
        if lst2[x] == 6: lst2[x] = 9
        elif lst2[x] == 9: lst2[x] = 6
    
    return lst1 == lst2[::-1]

def solve(a, b):
    invalid_digits = {2, 3, 4, 5, 7}
    lst = [i for i in range(a, b) if invalid_digits == (invalid_digits - {int(k) for k in str(i)}) and (not len(str(i)) % 2 or (str(i)[len(str(i))//2] not in ['6', '9'])) and mirror(i)]
    print(lst)
    return len(lst)

print(solve(60000,70000))