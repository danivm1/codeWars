def digital_root_rec(n):
    s = 0
    while n:
        s += n % 10
        n //= 10

    return s if s < 10 else digital_root_rec(s)


def digital_root(n): return n % 9 or n and 9


print(digital_root(168274512735))