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
print(next(gen))