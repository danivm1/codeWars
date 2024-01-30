def gcd(a, b):
    if b != 0:
        return gcd(b, a%b)
    return a, b

def mixed_fraction(s: str):
    a, b = s.split("/")
    
    sign = False

    if "-" in a:
        a = a.strip("-")
        sign = not sign

    if "-" in b:
        b = b.strip("-")
        sign = not sign

    a = int(a)
    b = int(b)

    if not a % b: 
        return f"{'-' if sign else ''}{a//b}" if a != 0 else "0"

    div = gcd(a, b)[0]

    a //= div
    b //= div

    return f"{'-' if sign else ''}{str(a//b) + ' ' if a > b else ''}{a%b}/{b}"

print(mixed_fraction("42/9"))



    #Input: 42/9, expected result: 4 2/3'