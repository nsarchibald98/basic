def factorial(x):
    """
    The function calls on the function.
    :param x: integer
    :return: integer and the factorial of said integer
    """
    if x == 1:
        return 1
    else:
        return x * (factorial(x - 1))


num = 4
print('The factorial of ', num, ' is', factorial(num))
