from functools import wraps


def type_check(correct_type):
    def type_check_decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, correct_type):
                raise InvalidTypeError(f"Expected: {correct_type}.")
            return func(arg)
        return wrapper
    return type_check_decorator


class InvalidTypeError(Exception):
    pass


@type_check(int)
def times2(num):
    return num * 2


if __name__ == "__main__":
    try:
        # correct
        print(times2(10))

        # incorrect
        print(times2("moshe"))

    except InvalidTypeError as error:
        print(error)