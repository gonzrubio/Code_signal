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
    # Empty tree or single node are symmetric
    if root is None or (root.left is None and root.right is None):
        return True
    # Only one child of root exists
    elif root.left is None and root.right is not None or \
         root.right is None and root.left is not None:
             return False
    else:
        # Enque both childre of root since they exist
        q = deque([root.left, root.right])

        while q:
            left_node = q.popleft()
            right_node = q.popleft()

            if left_node.value != right_node.value:
                return False
            else:
                # Append left child of left subtree and right child of right
                # subtree if they both exist
                if left_node.left is not None and right_node.right is not None:
                    q.append(left_node.left)
                    q.append(right_node.right)  
                # If only one exists then its asymmetric
                elif left_node.left is None and right_node.right is not None or \
                     left_node.left is not None and right_node.right is None:
                         return False
                    
                # Append right child of left subtree and left child of right
                # subtree if they both exist
                if left_node.right is not None and right_node.left is not None:
                    q.append(left_node.right)
                    q.append(right_node.left)
                elif left_node.right is None and right_node.left is not None or \
                     left_node.right is None and right_node.left is not None:
                         return False

    return True


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

    # root = Vertex()
    # root.value = 1
    # root.left = Vertex()
    # root.left.value = 2
    # root.left.left = Vertex()
    # root.left.left.value = 3
    # root.left.left.left = None
    # root.left.left.right = None
    # root.left.right = Vertex()
    # root.left.right.value = 4
    # root.left.right.left = None
    # root.left.right.right = None

    # root.right = Vertex()
    # root.right.value = 2
    # root.right.left = Vertex()
    # root.right.left.value = 4
    # root.right.left.left = None
    # root.right.left.right = None
    # root.right.right = Vertex()
    # root.right.right.value = 3
    # root.right.right.left = None
    # root.right.right.right = None

    # root = Vertex()
    # root.value = 1000
    
    # root = Vertex()
    # root.value = 0
    # root.left = Vertex()
    # root.left.value = 6

    # root = Vertex()
    root = None

    print(is_tree_symmetric(root))

