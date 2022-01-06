def myGenerator():
    print("First item")
    yield 10

    print("Second item")
    yield 20

    print("Third item")
    yield 30

gen = myGenerator()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

def myGenerator():
    print("First item")
    yield 10

    return

    print("Second item")
    yield 20

    print("Third item")
    yield 30

gen = myGenerator()

print(next(gen))
# print(next(gen))
# print(next(gen))
print("----")

def generate_sequence():
    n = 1
    yield n

    n = n + 2
    yield n

    n = n + 3
    yield n

gen = generate_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print("----")

def generate_cubes():
    for n in range(10):
        yield n ** 3

gen = generate_cubes()
# print(next(gen))

cube_list = list(gen)
print(cube_list)

another_cube_list = list(gen)
print(another_cube_list)

gen = generate_cubes()
cube_tuple = tuple(gen)
print(cube_tuple)