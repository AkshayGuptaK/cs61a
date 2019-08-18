from operator import add, mul


def make_skipper(n):
    """
    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    def skipper(k):
        i = 0
        while i <= k:
            if i % n != 0:
                print(i)
            i += 1
    return skipper


def make_alternator(f, g):
    """
    >>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
    >>> a(5)
    1
    6
    9
    8
    25
    >>> b = make_alternator(lambda x: x * 2, lambda x: x + 2)
    >>> b(4)
    2
    4
    6
    6
    """
    def alternator(x):
        i = 1
        while i <= x:
            if i % 2 == 0:
                print(g(i))
            else:
                print(f(i))
            i += 1
    return alternator


def mario_number(level):
    """
    Return the number of ways that Mario can traverse the level,
    where Mario can either hop by one digit or two digits each turn.
    A level is defined as being an integer with digits where a 1 is
    something Mario can step on and 0 is something Mario cannot step
    on.
    >>> mario_number(10101) # Hops each turn: (1, 2, 2)
    1
    >>> mario_number(11101) # Hops each turn: (1, 1, 1, 2), (2, 1, 2)
    2
    >>> mario_number(100101)# No way to traverse through level
    0
    """
    if level == 1:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        return mario_number(level // 10) + mario_number(level // 100)


def combine(n, f, result):
    """
    Combine the digits in n using f.
    >>> combine (3, mul, 2) # mul (3, 2)
    6
    >>> combine (43, mul, 2) # mul (4, mul (3, 2))
    24
    >>> combine (6502, add, 3) # add (6, add (5, add (0, add (2 , 3)))
    16
    >>> combine (239, pow, 0) # pow (2, pow (3, pow (9, 0)))
    8
    """
    if n == 0:
        return result
    else:
        return combine(n // 10, f, f(n % 10, result))
