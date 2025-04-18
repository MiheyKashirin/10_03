def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    for _ in range(end):
        yield begin
        begin = func(begin)
from inspect import isgenerator
gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True
assert list(gen) == [2, 4, 16, 256]
print('OK')
gen=some_gen(3,3,pow)
assert list(gen)==[3,9,81]
print('ok')