def example_2(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@example_2
def say_hello():
    print("Hello, World!")

say_hello()