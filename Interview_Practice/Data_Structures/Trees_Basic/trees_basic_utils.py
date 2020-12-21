"""Module with basic trees functionality."""


class Tree(object):
    """Binary tree."""

    def __init__(self, x):
        """Create a new node."""
        self.value = x
        self.left = None
        self.right = None

