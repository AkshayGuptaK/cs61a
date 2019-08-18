from math import sqrt


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(k):
        if n == 1 or n % k == 0:
            return False
        elif k > sqrt(n):
            return True
        else:
            return prime_helper(k+1)
    return prime_helper(2)


def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n == 0:
            return x
        else:
            return f(repeat(n-1))
    return repeat


def count_stair_ways(n):
    """
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    """
    if n <= 1:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    return sum([count_k(n-i, k) for i in range(1, k+1)])


def pascal(row, column):
    """
    >>> pascal(0, 0)
    1
    >>> pascal(3, 4)
    0
    >>> pascal(4, 2)
    6
    """
    if column < 0 or column > row:
        return 0
    elif column == 0 and row == 0:
        return 1
    return pascal(row-1, column) + pascal(row-1, column-1)
