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

display_function_python = get_favorite_programming_language("Python")
display_function_python()

display_function_python = get_favorite_programming_language("Java")
display_function_python()

del get_favorite_programming_language
# get_favorite_programming_language()

display_function_python()
