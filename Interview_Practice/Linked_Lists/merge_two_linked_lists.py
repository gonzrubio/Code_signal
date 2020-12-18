"""Merge two linked lists.

Merge two singly linked lists sorted in non-decreasing order.
Note: Solve in O(|l1| + |l2|) time complexity.
"""


import linked_list_utils as ll
from linked_list_utils import ListNode


def mergeTwoLinkedLists(l1, l2):
    """Return a singly linked list sorted in non-decreasing order.

    The resulting list contains all elements from both original lists.
    """
    # Deal with empty lists.
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    head = ListNode(None)
    tail = head
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach tail to remaining elements of no-empty linked list.
    tail.next = l1 if l1 else l2
    return head.next


def tests():
    """Sample Tests."""
    test_cases = [([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
                  ([1, 1, 2, 4], [0, 3, 5], [0, 1, 1, 2, 3, 4, 5]),
                  ([5, 10, 15, 40], [2, 3, 20], [2, 3, 5, 10, 15, 20, 40]),
                  ([1, 1], [2, 4], [1, 1, 2, 4]),
                  ([], [1, 1, 2, 2, 4, 7, 7, 8], [1, 1, 2, 2, 4, 7, 7, 8]),
                  ([], [], []),
                  ([1, 1, 4], [], [1, 1, 4]),
                  ([1, 1], [0], [0, 1, 1]),
                  ([0], [2], [0, 2]),
                  ([1], [-100000000, 100000000], [-100000000, 1, 100000000]),
                  ([-1, 0, 1], [-1, 0, 0, 1], [-1, -1, 0, 0, 0, 1, 1])]

    for l1, l2, expected in test_cases:
        res = mergeTwoLinkedLists(ll.list_to_link(l1), ll.list_to_link(l2))
        expected = ll.list_to_link(expected)

        if not ll.are_equal(res, expected):
            ll.print_linked_list(res)
            ll.print_linked_list(expected)


if __name__ == "__main__":
    tests()
