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