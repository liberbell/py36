# @non_negative_argument
def compute_rectangle_area(lenght, breadth):
    return lenght * breadth

def non_negative_argument(decorated_fn):
    def check_non_negative(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Argument cannot be negative or zero")

            return decorated_fn(*args)

        return check_non_negative

def display_important_message():
    print("This is an important message.")

display_important_message()

def display_boring_message():
    print("This is a boring message....")

display_boring_message()

def display_entertaing_message():
    print("This is an entertaining message....")

display_entertaing_message()

def emphasize_message(display_fn):
    print("*******************************")
    display_fn()
    print("*******************************")

emphasize_message(display_important_message)