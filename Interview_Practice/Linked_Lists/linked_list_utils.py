"""Module with linked lists functionality."""


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
    print("NULL")


def reverse_linked_list(head):
    """Return the head of the reversed linked list."""
    prev = None
    node = head
    while node:
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
    return prev


print_linked_list(reverse_linked_list(list_to_link([1, 2, 3, 4, 5])))
