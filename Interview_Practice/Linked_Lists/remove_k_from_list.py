"""Remove k from list.

Given a singly list of integers l, and an integer k,
remove all elements from list l that have a value equal to k.

Note: Solve in O(n) time and O(1) additional space.
"""


class ListNode(object):
    """Linked list class."""

    def __init__(self, x):
        """Value of current node and pointer to next node."""
        self.value = x
        self.next = None


def list_to_link(python_list):
    """Return a Link from a Python list with the same elements."""
    curr = root = ListNode(0)
    for e in python_list:
        curr.next = ListNode(e)
        curr = curr.next
    return root.next


def print_linked_list(head):
    """Print elements of a linked list."""
    curr = head
    while curr:
        print(curr.value, end="->")
        curr = curr.next
    print()


def removeKFromList(head, k):
    """Return list with all occurences of k removed."""
    new_head = ListNode(0)
    new_head.next = head
    curr = new_head
    while curr:
        while curr.next and curr.next.value == k:
            curr.next = curr.next.next
        curr = curr.next
    return new_head.next


def tests():
    """Sample Tests."""
    # python_list = [3, 1, 2, 3, 4, 5]
    # k = 3
    # python_list = [1000, 1000]
    # k = 1000
    # python_list = [123, 456, 789, 0]
    # k = 0
    # python_list = []
    # k = 0
    python_list = [0]
    k = 0
    print_linked_list(list_to_link(python_list))
    print_linked_list(removeKFromList(list_to_link(python_list), k))


if __name__ == "__main__":
    tests()
