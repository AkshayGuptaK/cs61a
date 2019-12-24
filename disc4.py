# Constructor
def tree(label, branches=[]):
#     for branch in branches:
        # assert is_tree(branch)
    return [label] + list(branches)
# Selectors
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
# For convenience
def is_leaf(tree):
    return not branches(tree)

def tree_max(t):
    """Return the maximum label in a tree.
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    if is_leaf(t):
        return label(t)
    return max(label(t), max([tree_max(b) for b in branches(t)]))

def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])

def square_tree(t):
    """Return a tree with the square of every element in t
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> square_tree(t)
    [16, [4, [1]], [100]]
    """
    return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])

# def find_path(tree, x):
#     """
#     >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
#     >>> find_path(t, 5)
#     [2, 7, 6, 5]
#     >>> find_path(t, 10) # returns None
#     """
#     if _____________________________:
#         return _____________________________
#     _____________________________:
#         path = _____________________________
#         if _____________________________:
#             return _____________________________

def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [x]
    else:
        path = [label(tree)]
        if not is_leaf(tree):
            return path + [find_path(b, x) for b in branches(tree)]

def prune(t, k):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> prune(t, 2)
    [2, [7, [3], [6]], [15]]
    """
    if k == 0:
        return tree(label(t))
    return tree(label(t), [prune(b, k-1) for b in branches(t)])

def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will
    reach N, with height H.
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    if h == 0:
        return tree(n)
    if (n-1)%3 == 0 and (n-1)/3 > 1 and (n-1)/3 % 2 != 0:
        return tree(n, [hailstone_tree(2*n, h-1), hailstone_tree(int((n-1)/3), h-1)])
    return tree(n, [hailstone_tree(2*n, h-1)])