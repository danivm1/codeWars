def hex5(x): return x * 0x55555556 >> 32

def hexA(x): return x * 0xAAAAAAAB >> 33


x = 432
print(hex5(x))
print(hexA(x))