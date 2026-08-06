def decorator(func):

    def wrapper():
        print("===== Start =====")

        func()

        print("===== End =====")

    return wrapper


@decorator
def welcome():
    print("Welcome Python!")

welcome()