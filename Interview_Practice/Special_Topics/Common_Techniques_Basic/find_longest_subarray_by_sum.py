"""Find longest subarray by sum.

You have an unsorted array arr of non-negative integers and a number s.
Find a longest contiguous subarray in arr that has a sum equal to s.
Return two integers that represent its inclusive bounds. If there are several
possible answers, return the one with the smallest left bound. If there are no
answers, return [-1].

Your answer should be 1-based, meaning that the first position of the array
is 1 instead of 0.

Created on Sun Sep 26 19:58:34 2021

@author: gonzo
"""


def findLongestSubarrayBySum(s, arr):
    """Return a two-element array that represent the bounds of the subarray."""
    ans = [-1]

    for left in range(len(arr)):
        curr_sum = arr[left]
        if curr_sum == s and len(ans) == 1:
            ans = [left + 1] * 2

        for right in range(left + 1, len(arr)):
            curr_sum += arr[right]

            if curr_sum == s:
                # First found soltion
                if len(ans) == 1:
                    ans = [left + 1, right + 1]
                # Left bound is right bound
                elif ans[1] == ans[0]:
                    ans = [left + 1, right + 1]
                # Longer subarray
                elif ans[1] - ans[0] < right - left:
                    ans = [left + 1, right + 1]

            elif curr_sum > s:
                break

    return ans


if __name__ == '__main__':

    # s = 12  # ans = [2, 4]
    # arr = [1, 2, 3, 7, 5]

    # s = 15  # ans = [1, 5]
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # s = 15  # ans = [1, 8]
    # arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]

    # s = 3   # ans = -1
    # arr = [1, 1]

    # s = 3   # ans = -1
    # arr = [2]

    # s = 468    # ans = [42, 46]
    # arr = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28,
    #         162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22,
    #         117, 119, 96, 48, 127, 0, 172, 0, 139, 0, 0, 70, 113, 68,
    #         100, 36, 95, 104, 12, 123, 134]

    # s = 3  # ans = [1, 1]
    # arr = [3]

    # s = 0     # ans = [2, 2]
    # arr = [1, 0, 2]

    s = 3    # ans = [1, 3]
    arr = [0, 3, 0]

    print(findLongestSubarrayBySum(s, arr))
