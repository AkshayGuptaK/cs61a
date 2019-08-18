aaron, burr = 2, 5
aaron, burr = 4, aaron + 1
hamil = 10

def alex(hamil):
    def g(w):
        hamil = 2 * w
        print(hamil, w)
        w = hamil
        return hamil
    w = 5
    alex = g(w + 1)
    print(w, alex, hamil) # 5 12 3

def el(i, za):
    def angelica():
        return i + 1
    if i > 10:
        return za()
    elif i > 4:
        print(angelica())
        return el(i * i, za)
    else:
        return el(i * i, angelica)

K = lambda x: lambda y: x

def pr(x):
    print(x)
    return x

# Q3 onwards

def triangle(a, b, c):
    """Return whether a, b, and c could be the legs of a triangle.
    >>> triangle(3, 4, 5)
    True
    >>> triangle(3, 4, 6)
    True
    >>> triangle(6, 3, 4)
    True
    >>> triangle(3, 6, 4)
    True
    >>> triangle(9, 2, 2)
    False
    >>> triangle(2, 4, 2)
    False
    """
    longest = max(a, b, c)
    sum_of_others = a + b + c - longest # or min(a+b, a+c, b+c)
    return longest < sum_of_others

def collapse(n):
    """For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.
    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """
    left, last = n // 10, n % 10

    if left == 0:
        return last
    elif left % 10 == last:
        return collapse(left)
    else:
        return collapse(left) * 10 + last

def find_pair(p):
    """Given a two-argument function P, return a function that takes a
    non-negative integer and returns True if and only if two adjacent digits
    in that integer satisfy P (that is, cause P to return a true value).
    >>> z = find_pair(lambda a, b: a == b) # Adjacent equal digits
    >>> z(1313)
    False
    >>> z(12334)
    True
    >>> z = find_pair(lambda a, b: a > b)
    >>> z(1234)
    False
    >>> z(123412)
    True
    >>> find_pair(lambda a, b: a <= b)(9753)
    False
    >>> find_pair(lambda a, b: a == 1)(1) # Only one digit; no pairs.
    False
    """
    def find(n):
        while n > 9:
            if p((n // 10) % 10, n % 10):
                return True
            else:
                n = n // 10
        return False

    return find

def confirmer(code):
    """Return a confirming function for CODE.
    >>> confirmer(204)(2)(0)(4) # The digits of 204 are 2, then 0, then 4.
    True
    >>> confirmer(204)(2)(0)(0) # The third digit of 204 is not 0.
    False
    >>> confirmer(204)(2)(1) # The second digit of 204 is not 1.
    False
    >>> confirmer(204)(20) # The first digit of 204 is not 20.
    False
    """
    def confirm1(d, t):
        def result(digit):
            if d == digit:
                return t
            else:
                return False
        return result

    def extend(prefix, rest):
        """Return a confirming function that returns REST when given the digits of PREFIX.
        For example, if c = extend(12, confirmer(34)), then c(1)(2) returns confirmer(34),
        so that c is a confirming function for 1234."""
        left, last = prefix // 10, prefix % 10
        if left == 0:
            return confirm1(last, rest)
        else:
            return extend(left, confirm1(last, rest))

    return extend(code, True)

def decode(f, y=0):
    """Return the code for a confirming function f.
    >>> decode(confirmer(12001))
    12001
    >>> decode(confirmer(56789))
    56789
    """
    d = 0
    while d < 10:
        x, code = f(d), 10*y + d
        if x == True:
            return code
        elif x == False:
            d += 1
        else:
            return decode(x, code)