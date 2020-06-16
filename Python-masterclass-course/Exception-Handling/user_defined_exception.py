class NegativeNumberException(Exception):
    """number is negative """
    pass


def add(a,b):
    try:
        if a<0 or b<0:
            raise NegativeNumberException
    except (NegativeNumberException):
        print("a negative number")

add(-1,4)
