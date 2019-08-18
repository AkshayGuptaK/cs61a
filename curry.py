from inspect import signature


def curryN(f, args, n):
    if n == 0:
        return f(*args)
    return lambda x: curryN(f, args + [x], n-1)


def curry(f):
    num_args = len(signature(f).parameters)
    return curryN(f, [], num_args)


def add_five_numbers(a, b, c, d, e):
    return a + b + c + d + e

print(curry(add_five_numbers)(1)(2)(3)(4)(5))
