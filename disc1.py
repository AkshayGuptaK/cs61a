def wears_jacket_with_if(temp, raining):
    """Decides whether to wear jacket
    >>> wears_jacket_with_if(50, False)
    True
    >>> wears_jacket_with_if(70, True)
    True
    >>> wears_jacket_with_if(70, False)
    False
    """
    return temp < 60 or raining

from math import sqrt

def is_prime(n):
    """Returns whether n is a prime number
    >>> is_prime(13)
    True
    >>> is_prime(4)
    False
    """
    k = 2
    while k <= sqrt(n):
        if n % k == 0:
            return False
        k += 1
    return True

def count_digits(n):
    """
    >>> count_digits(42)
    2
    >>> count_digits(12345678)
    8
    >>> count_digits(1)
    1
    """
    digits = 1
    while n >= 10 ** digits:
        digits += 1
    return digits

def count_matches(n, m):
    """
    >>> count_matches(10, 30)
    1
    >>> count_matches(12345, 23456)
    0
    >>> count_matches(212121, 321321)
    2
    >>> count_matches(101, 11) # only one’s place matches
    1
    >>> count_matches(101, 10) # no place matches
    0
    """
    matches = 0
    divisor = 10
    while n >= divisor and m >= divisor:
        if n % divisor == m % divisor:
            matches += 1
        divisor *= 10
    return matches
