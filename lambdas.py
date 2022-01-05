def increment_fn(x):
    return x + 1

print(increment_fn)
increment_fn = lambda x : x + 1
print(increment_fn)
print(increment_fn(10))
# print(increment_fn(10, 2))

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def square_root(number):
    return number ** (1/2)

def cube_root(number):
    return number ** (1/3)

def raise_to_n(number):
    return number ** n

square = lambda x: x ** 2
cube = lambda x: x ** 3
raise_to_n = lambda x, n: x ** n

print(square(3))