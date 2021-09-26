"""Has path with given sum.

Created on Sat Sep 25 15:21:55 2021

@author: gonzr

Given a binary tree t and an integer s, determine whether there is a root to
leaf path in t such that the sum of vertex values equals s.
"""


from collections import deque


class Vertex:
    """Vertex object in a binary tree."""

    def __init__(self):
        """Initialize Vertex object.
        Fields
        ----------
        value : int
            The value of node v
        left : None
            The left child of node v
        right : None
            The right child of node v            
        """
        self.value = None
        self.left = None
        self.right = None


def has_path_with_given_sum(tree, s):
    """Return true if there is a path from root to leaf with given sum."""

    visited = [False] * len(tree)
    node_stack = deque([0])
    visited[0] = True
    sum_stack = deque([tree[0].value])

    while node_stack:
        curr = node_stack.pop()
        curr_sum = sum_stack.pop()
        
        if tree[curr].left is None and tree[curr].right is None  and curr_sum == s:
                return True
            
        for child in [tree[curr].left, tree[curr].right]:
            if child and not visited[child]:
                visited[child] = True
                node_stack.append(child)
                sum_stack.append(curr_sum + tree[child].value)

    return False


if __name__ == '__main__':
    # data = [[4, 1, 2], [1, 3, None], [3, 4, 5], [-2, None, 6], [1, None, None],
    #         [2, 7, 8], [3, None, None], [-4, None, None], [-3, None, None]]
    # s = 7

    # data = [[10, 1, 2], [8, 3, 4], [2, 5, None], [3, None, None],
    #         [5, None, None], [2, None, None]]
    # s = 21
    
    # data = [[8, None, 1], [3, None, None]]
    # s = 8
    
    data = [[5, 1, None], [7, None, None]]
    s = 5
    
    tree = [Vertex() for node in range(len(data))]
    for ii in range(len(data)):
        tree[ii].value = data[ii][0]
        tree[ii].left = data[ii][1]
        tree[ii].right = data[ii][2]    

    print(has_path_with_given_sum(tree, s))









