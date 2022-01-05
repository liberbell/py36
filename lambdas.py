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
print(cube(9))
print(raise_to_n(2, 16))

create_list_fn = lambda some_string, times: [some_string for _ in range(times)]
print(create_list_fn("Yeah!", 4))

print((lambda x: x * 10)(33))
print((lambda x, y: x % y)(33, 5))

create_student_record_fn = lambda name, major, university: {"name": name, "major": major, "university": university}
student_1 = create_student_record_fn("Bob", "History", "Cornell")
print(student_1)