"""Sum of two.

Given two integer arrays, a and b, and an integer target value v. Determine
whether there is a pair of numbers, where one number is taken from a and the
other from b, that can be added together to get a sum of v. Return true if such
a pair exists, otherwise return false.

Constraints: 0 ≤ |a|, |b| ≤ 10^5, -10^9 ≤ a[i], b[i], v ≤ 10^9.
"""


def sum_of_two(array_a, array_b, target):
    """Return True if a[i]+b[j]=v, False otherwise."""
    if not array_a or not array_b:
        return False
    array_a = [target - elem for index, elem in enumerate(array_a)]
    return bool(set(array_a) & set(array_b))


def tests():
    """Sample Tests."""
    samples = [([1, 2, 3], [10, 20, 30, 40], 42, True),
               ([], [], 0, False),
               ([], [1], 1, False),
               ([1], [1], 1, False),
               ([-10e9]*(10 ^ 5), [10e9]*(10 ^ 5), 0, True)]
    for array_a, array_b, target, expected in samples:
        output = sum_of_two(array_a, array_b, target)
        if output != expected:
            print(f"array_a={array_a}, array_b={array_b}, target={target}\
                  output={output}, expected={expected}")


if __name__ == "__main__":
    tests()
