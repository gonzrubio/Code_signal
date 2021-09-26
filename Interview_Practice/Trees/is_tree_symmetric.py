"""Is the tree symmetric.

Given a binary tree t, determine whether it is symmetric around its center,
i.e. each side mirrors the other.

Created on Sun Sep 26 09:45:48 2021

@author: gonzo
"""


from collections import defaultdict, deque


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


def is_tree_symmetric(root):
    """Use bfs to see that each level is around the centre symmetric."""
    if root is None or (root.left is None and root.right is None):
        return True
    else:
        # Enqueue the left and right children of the root since its not empty
        q = deque([root.left, root.right])

        while q:
            left = deque.popleft()
            right = deque.popleft()
            if left.value == right.value:
                pass


if __name__ == '__main__':

    # t = {
    #     "value": 1,
    #     "left": {
    #         "value": 2,
    #         "left": {
    #             "value": 3,
    #             "left": None,
    #             "right": None
    #         },
    #         "right": {
    #             "value": 4,
    #             "left": None,
    #             "right": None
    #         }
    #     },
    #     "right": {
    #         "value": 2,
    #         "left": {
    #             "value": 4,
    #             "left": None,
    #             "right": None
    #         },
    #         "right": {
    #             "value": 3,
    #             "left": None,
    #             "right": None
    #         }
    #     }
    # }

    # t = {"value": 1,
    #      "left": {
    #          "value": 2,
    #          "left": None,
    #          "right": {
    #              "value": 3,
    #              "left": None,
    #              "right": None
    #              }
    #          },
    #      "right": {
    #          "value": 2,
    #          "left": None,
    #          "right": {
    #              "value": 3,
    #              "left": None,
    #              "right": None
    #              }
    #          }
    #      }

    # Manually build tree for now
    print(is_tree_symmetric(tree[0]))

