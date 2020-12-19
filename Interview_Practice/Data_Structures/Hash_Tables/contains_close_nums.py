"""Contains close nums.

Given an array of integers nums and an integer k, determine whether there are
two distinct indices i and j in the array where nums[i] = nums[j] and the
absolute difference between i and j is less than or equal to k.

Constraints: 0<= |nums| <= 55000, -2^31 - 1 ≤ nums[i] ≤ 2^31 - 1, 0 ≤ k ≤ 35000
"""


def containsCloseNums(nums, k):
    """Return true if |i-j|<k+1 for nums[i]=nums[j] or False otherwise."""
    nums_dict = dict()
    for index, number in enumerate(nums):
        if number not in nums_dict:
            nums_dict[number] = index
            continue
        if abs(nums_dict[number]-index) < k+1:
            return True
        nums_dict[number] = index
    return False


def tests():
    """Sample Tests."""
    samples = [([0, 1, 2, 3, 5, 2], 3, True),
               ([0, 1, 2, 3, 5, 2], 2, False),
               ([], 0, False),
               ([0], 2, False),
               ([2, 2], 2, True),
               ([1, 2], 1, False),
               ([0]*55000, 35000, True),
               ([-1, -1], 1, True),
               ([1, 2, 1], 1, False),
               ([1, 2, 1], 0, False),
               ([1, 0, 1, 1], 1, True)]
    for nums, k, output in samples:
        if containsCloseNums(nums, k) != output:
            print(f"nums={nums}, k={k}, output={output}")


if __name__ == "__main__":
    tests()
