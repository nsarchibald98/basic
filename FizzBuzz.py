def fizzbuzz(m: int, n: int):
    """
    Write a program that prints the numbers from 1 to 100. \
    But for multiples of three print “Fizz” instead of the \
    number and for the multiples of five print “Buzz”. \
    For numbers which are multiples of both three and five print “FizzBuzz \n
    :param n: Starting Value
    :param m: Ending Value
    :return: If divisable by 3 = Fizz, if divisable by 5 = Buzz, if divisable by both then FizzBuzz
    """
    for i in range(m, n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


# fizzbuzz(1, 101)


def lamfizz(m: int, n: int):
    """
    Flex on your friends with this bad boi \n
    :param m: Starting integer
    :param n: Ending integer
    :return: Buzz, Fizz, or the integer
    """
    print(*map(lambda i: 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i, range(m, n)), sep='\n')


# lamfizz(1, 101)


def another(m: int, n: int):
    """
    Aww shit, here we go again \n
    :param m: Starting integer
    :param n: Ending integer
    :return: Fizz, Buzz, Fizzbuzz
    """
    for i in range(m, n):
        fizz = 'Fizz' if i % 3 == 0 else ''
        buzz = 'buzz' if i % 5 == 0 else ''
        print(f'{fizz}{buzz}' or i)


another(1, 101)