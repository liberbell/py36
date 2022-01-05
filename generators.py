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

def generate_sequence():
    n = 1
    yield 10

    n = n + 2
    yield 20

    n = n + 3
    yield 30

gen = generate_sequence()
print(next(gen))
print(next(gen))
print(next(gen))