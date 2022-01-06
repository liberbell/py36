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

gen = generate_cubes()
for cube in gen:
    print(cube)

def generate_powers_of_two(limit):
    for num in range(limit):
        yield 2 ** num

print(generate_powers_of_two(8))
gen = generate_powers_of_two(10)
print(gen)

for i in gen:
    print(i)

def generate_inifinite_power_of_two():
    num = 0
    while True:
        num = num + 1
        yield 2 ** num

# gen = generate_inifinite_power_of_two()
# print(gen)

# for num in gen:
#     print(num)

def arithmetic_progression(start, step, limit):
    count = 1
    while count <= limit:
        yield start

        start += step
        count += 1

for i in arithmetic_progression(1, 2, 10):
    print(i)

def message_receiver():
    while True:
        value = yield
        print(f"Receved this message: {value}")