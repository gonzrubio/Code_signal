"""Remove k from list.

Given a singly list of integers l, and an integer k,
remove all elements from list l that have a value equal to k.

Note: Solve in O(n) time and O(1) additional space.
"""

import linked_list_utils as ll
from linked_list_utils import ListNode


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
    ll.print_linked_list(ll.list_to_link(python_list))
    ll.print_linked_list(removeKFromList(ll.list_to_link(python_list), k))


if __name__ == "__main__":
    tests()
