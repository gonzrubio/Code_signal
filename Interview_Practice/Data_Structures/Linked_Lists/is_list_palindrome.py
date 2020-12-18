"""Determine if List is a Palindrome.

Given a singly linked list of integers, determine whether it's a palindrome.
Note: Solve in O(n) time using O(1) additional space.
"""


import linked_list_utils as ll


def isListPalindrome(head):
    """Return True if it is a palindrome, otherwise return False."""
    node = head
    fast = node
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        # Reverse elemets of first half of list.
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    # Deal with even or odd number of elements.
    tail = node.next if fast else node

    # Compare reversed half and remanining elements.
    return ll.are_equal(prev, tail)


def tests():
    """Sample Tests."""
    test_cases = [([], True),
                  ([1], True),
                  ([1, 1], True),
                  ([1, 2], False),
                  ([3, 7, 3], True),
                  ([3, 7, 4], False),
                  ([6, 3, 7, 3, 6], True),
                  ([7, 8, 6, 3, 7, 3, 6, 8, 7], True),
                  ([7, 8, 6, 3, 7, 4, 6, 8, 7], False)]
    for inp, expected in test_cases:
        res = isListPalindrome(ll.list_to_link(inp))
        if res != expected:
            print("%s: %d != %d" % (inp, res, expected))


if __name__ == "__main__":
    tests()
