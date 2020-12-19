"""Contains duplicates.

Given an array of integers, write a function that determines whether the array
contains any duplicates. Your function should return true if any element
appears at least twice in the array, and it should return false if every
element is distinct.

Constarints: 0 ≤ |a| ≤ 10^5, -2*10^9 ≤ a[i] ≤ 2*10^9.
"""


def containsDuplicates(array):
    """Return True if array contains duplicates or False otherwise."""
    return len(set(array)) != len(array)


def tests():
    """Sample Tests."""
    samples = [([], False),
               ([1], False),
               ([1] * (10 ^ 5), True),
               ([-2 * (10 ^ 9), -2 * (10 ^ 9)], True),
               ([2 * (10 ^ 9), 1 * (10 ^ 9)], False),
               ([1, 2, 3, 4], False)]
    for array, output in samples:
        if containsDuplicates(array) != output:
            print(f"array={array}, output={output}")


if __name__ == "__main__":
    tests()
