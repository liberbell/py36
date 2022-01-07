def outer_fn():
    def display_favorite_programming_language():
        print("My favorite programming language is Python.")

    print("Executing the outer function")
    display_favorite_programming_language()

# print(outer_fn())
outer_fn()
display_favorite_programming_language()