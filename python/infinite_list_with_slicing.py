from typing import Generator

def infinite_generator(start: int, step: int) -> Generator[int, str, None]:
    i = start
    while 1:
        yield i
        i += step
        
a = infinite_generator(5, 2)
print(a[3:6])