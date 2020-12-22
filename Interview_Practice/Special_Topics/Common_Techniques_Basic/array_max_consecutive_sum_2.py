"""Array max consecutive sum 2.

Given an array of integers, find the maximum possible sum you can get from one
of its contiguous subarrays. The subarray from which this sum comes must
contain at least 1 element.

Constrains:
3 ≤ |array| ≤ 10^5, -1000 ≤ array[i] ≤ 1000
"""


def arrayMaxConsecutiveSum2(array):
    """Return the maximum subarray sum via Kadane's algorithm O(n)."""
    best_sum = -1000
    current_sum = 0
    for x in array:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


def tests():
    """Sample Tests."""
    samples = [([-2, 2, 5, -11, 6], 7),
               ([1, 1, 1], 3),
               ([1, 0, -1], 1),
               ([-3, -2, -1, -4], -1),
               ([1, -2, 3, -4, 5, -3, 2, 2, 2], 8),
               ([-1000]*100000, -1000),
               ([1000]*100000, 100000000),
               ([0]*100000, 0)]
    for array, expected in samples:
        answer = arrayMaxConsecutiveSum2(array)
        if answer != expected:
            print(f"array={array}, expected={expected}, answer={answer}")


if __name__ == "__main__":
    tests()
