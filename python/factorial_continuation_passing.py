import sys
sys.set_int_max_str_digits(1000000)

thunk = lambda name, *args: lambda: name(*args)

def _trampoline(bouncer):
    while callable(bouncer):
        bouncer = bouncer()
    return bouncer

trampoline = lambda f: lambda *args: _trampoline(f(*args))

identity = lambda x: x

_factorial = lambda n, c=identity: c(1) if n == 0 else thunk(_factorial, n - 1, lambda result: thunk(c, n * result))

factorial = trampoline(_factorial)

print(factorial(100000))