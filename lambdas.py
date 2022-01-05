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

create_student_record_fn = \
    lambda name, major = "History", university = "Cornell": {"name": name, "major": major, "university": university}

student_2 = create_student_record_fn("Eric")
print(student_2)

student_3 = create_student_record_fn("Alex", "Computer Science")
print(student_3)

create_student_list_fn = lambda *args : [name for name in args]
student_list = create_student_list_fn("George", "Ringo", "Ed")
print(student_list)

create_student_record_fn = lambda **kwargs : {key: value for key, value in kwargs.items()}

student_1 = create_student_record_fn(name="Bob", age=23)
print(student_1)

student_2 = create_student_record_fn(name="Alex", age=28, gpa=4.1)
print(student_2)

numbers = [2, -23, 45, 20, -19, 73, -89]
positive_numbers = filter(lambda x: x > 0, numbers)
print(list(positive_numbers))

sales_map = [
    {"country": "Mexico", "sales": 234.5},
    {"country": "United States", "sales": 567.5},
    {"country": "Canada", "sales": 110.5}
]
countries = map(lambda x: x["country"], sales_map)
print(countries)
