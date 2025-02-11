def decorator_ex(func):
    def wrapper(*args):
        print("Before adding")
        result = func(*args)
        print("Done!")
        print(str(args[0]) + " + " + str(args[1]) + " = " + str(result))
    return wrapper


@decorator_ex
def addition(x, y):
    print("Processing...")
    return x+y

addition(3,5)

