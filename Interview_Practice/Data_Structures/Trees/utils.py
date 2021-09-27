"""Module with basic trees functionality."""


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

    t = {"value": 1,
         "left": {
              "value": 2,
              "left": None,
              "right": {
                  "value": 3,
                  "left": None,
                  "right": None
                  }
              },
         "right": {
              "value": 2,
              "left": None,
              "right": {
                  "value": 3,
                  "left": None,
                  "right": None
                  }
              }
          }

    # Fix veretx class and make read from dict function
    # Implement tree height and tree size recursively (2-liners)

    print(is_tree_symmetric(root))
