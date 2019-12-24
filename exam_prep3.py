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

def complete(t, d, k):
    """Return whether t is d-k-complete.

    >>> complete(tree(1), 0, 5)
    True
    >>> u = tree(1, [tree(1), tree(1), tree(1)])
    >>> [ complete(u, 1, 3), complete(u, 1, 2), complete(u, 2, 3) ]
    [True, False, False]
    >>> complete(tree(1, [u, u, u]), 2, 3)
    True
    """
    if not branches(t):
        return d == 0
    bs = [ complete(b, d-1, k) for b in branches(t) ]
    return len(branches(t)) == k and all(bs)

"""
x,y,z = 1,2,3
x = [2, y, [[]]]
y = [1, [2, [3, []]]]
z = 0

y = [x, [y, [z, []]]]
x = [y[x][len(y[x][x][x])], y, [y[x][x][x]]]
z = x.count(z)
"""

def closest(t):
    """ Return the smallest difference between an entry and sum of the entries of its branches.

    >>> t = tree(8, [tree(4), tree(3)])
    >>> closest(t) # |8 - (4 + 3)| = 1
    1
    >>> closest(tree(5, [t])) # Same minimum as t
    1
    >>> closest(tree(10, [tree(2), t])) # |10 - (2 + 8)| = 0
    0
    >>> closest(tree(3)) # |3 - 0| = 3
    3
    >>> closest(tree(8, [tree(3, [tree(1, [tree(5)])])])) # | 3 - 1 | = 2
    2
    >>> sum([])
    0
    """
    diff = abs(label(t) - sum([ label(branch) for branch in branches(t) ]))
    return min([diff] + [closest(b) for b in branches(t)])

def is_path(t, path):
    """Return whether a given path exists in a tree, beginning at the root.
    >>> t = tree(1, [tree(2, [tree(4), tree(5)]), tree(3, [tree(6), tree(7)])])
    >>> is_path(t, [1, 2])
    True
    >>> is_path(t, [1, 2, 4])
    True
    >>> is_path(t, [2, 4])
    False
    """
    if label(t) != path[0]:
        return False
    if len(path) == 1:
        return True
    return any([is_path(b, path[1:]) for b in branches(t)])