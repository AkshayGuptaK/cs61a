def test_curry2():
    curry2 = lambda h: lambda x: lambda y: h(x, y)
    make_adder = curry2(lambda x, y: x + y)
    add_three = make_adder(3)
    five = add_three(2)
    return five


def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...   # Even numbers have remainder 0 when divided by 2.
    ...   return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1


def keep_ints_func(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...   # Even numbers have remainder 0 when divided by 2.
    ...   return x % 2 == 0
    >>> keep_ints_func(5)(is_even)
    2
    4
    """
    def keep_ints(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return keep_ints


def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    return multiply(m, n-1) + m


def countdown(n):
    """
    >>> countdown(7)
    7
    6
    5
    4
    3
    2
    1
    """
    if n == 1:
        print(1)

    if n > 1:
        print(n)
        countdown(n-1)


def countup(n):
    """
    >>> countup(3)
    1
    2
    3
    """
    if n == 1:
        return 1

    if n > 1:
        print(countup(n-1))
        return n


def sum_every_other_digit(n):
    """
    >>> sum_every_other_digit(7)
    7
    >>> sum_every_other_digit(30)
    0
    >>> sum_every_other_digit(228)
    10
    >>> sum_every_other_digit(123456)
    12
    >>> sum_every_other_digit(1234567) # 1 + 3 + 5 + 7
    16
    """
    if n < 10:
        return n
    return sum_every_other_digit(n // 100) + (n % 10)
