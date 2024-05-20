def next_higher(n):
    b = "0" + str(bin(n))[2:]
    index = -3
    while index < len(b) - 2:
        index = b.rfind('01')
        if not index:
            bSort = "".join(sorted(b[1:], reverse=True))
            if b[1:] == bSort:
                b = "10" + ("0" * bSort.count("0")) + ("1" * (bSort.count("1")-1))
                return int(b, 2)
            return int(b+"0", 2)
        
        b = b[:index] + "10" + b[index+2:]

    return int(b, 2)

print(next_higher(157286400))
# 159383553 1001100000000000000000000001