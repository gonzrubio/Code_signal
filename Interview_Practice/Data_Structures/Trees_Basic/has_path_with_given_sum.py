"""Has path with given sum.

Given a binary tree t and an integer s, determine whether there is a root to
leaf path in t such that the sum of vertex values equals s.
"""


def hasPathWithGivenSum(t, s):
    """Find path with given sum in the binary tree.

    Return true if there is a path from root to leaf in t such that the sum of
    node values in it is equal to s, otherwise return false.
    """
    if not t:
        return s == 0
    return hasPathWithGivenSum(t.left, s-t.value) or \
        hasPathWithGivenSum(t.right, s-t.value)
