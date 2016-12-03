
def factorial(n):
    """
    Find n!
    """

    if n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    """
    Finds the value of the nth term of the Fibonacci sequence
    """

    if n == 0:
        return 1

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def is_power_of_two(x):
    """
    Returns True if x is a power of two
    """

    if x == 1:
        return True

    if x % 2 != 0:
        return False

    return is_power_of_two(x / 2)
