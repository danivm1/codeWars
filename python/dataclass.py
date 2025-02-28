from dataclasses import asdict, dataclass, make_dataclass

@dataclass
class testClass:
    i: int

md = testClass(i=42)
md.__class__ = make_dataclass('test', [('s', str, None)], bases=(testClass,))

print(f'i: {md.i}\ns: {md.s}')
print(asdict(md))