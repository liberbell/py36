# def outer_fn():
#     def display_favorite_programming_language():
#         print("My favorite programming language is Python.")

#     print("Executing the outer function")
#     return display_favorite_programming_language()

# print(outer_fn())
# outer_fn()
# display_favorite_programming_language()

def get_favorite_programming_language():
    def display_favorite_programming_language():
        print("My favorite programming language is Python.")

    print("Executing the outer function")
    return display_favorite_programming_language

# display_fn = get_favorite_programming_language()
# print(display_fn)
# display_fn()

def get_favorite_programming_language():
    favorite_language = "Python"
    def display_favorite_programming_language():
        print(f"My favorite programming language is {favorite_language}.")

    print("Executing the outer function")
    return display_favorite_programming_language

# display_fn = get_favorite_programming_language()
# display_fn()

def get_favorite_programming_language(favorite_language):

    def display_favorite_programming_language():
        print(f"My favorite programming language is {favorite_language}.")

    print("Executing the outer function")
    return display_favorite_programming_language

# display_function_python = get_favorite_programming_language("Python")
# display_function_python()

# display_function_java = get_favorite_programming_language("Java")
# display_function_java()

del get_favorite_programming_language
# get_favorite_programming_language()

# display_function_python()

def add_employee_to_department(department_name):
    employee_list = []

    def add_employee(employee_name):
        employee_list.append(employee_name)

        print(f"Add {employee_name} to {department_name}")
        print(f"{department_name} employee: {employee_list}")

    return add_employee

add_to_sales_fn = add_employee_to_department("sales")
print(add_to_sales_fn)

add_to_engineering_fn = add_employee_to_department("engineering")
print(add_to_sales_fn)

# add_to_sales_fn("Alex")
# add_to_sales_fn("Eric")
# add_to_sales_fn("Ed")
# add_to_engineering_fn("George")
# add_to_engineering_fn("Bob")
# add_to_engineering_fn("Elton")

def formal_greeting():
    greeting = "How are you doing"

    def informal_greeting():
        greeting = "Hi there!"
        print("Greeting in the inner function: ", greeting)
    
    informal_greeting()
    print("Greeting in the outer function: ", greeting)

formal_greeting()

def formal_greeting():
    greeting = "How are you doing"

    def informal_greeting():
        nonlocal greeting

        greeting = "Hi there!"
        print("Greeting in the inner function: ", greeting)
    
    informal_greeting()
    print("Greeting in the outer function: ", greeting)

formal_greeting()

