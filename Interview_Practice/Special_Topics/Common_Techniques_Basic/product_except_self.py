"""Product except self.

You have an array nums. We determine two functions to perform on nums.
In both cases, n is the length of nums:

fi(nums) = nums[0] · nums[1] · ... · nums[i-1] · nums[i+1] · ... · nums[n-1].
(In other words, fi(nums) is the product of all array elements except the ithf.)

g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).

Using these two functions, calculate all values of f modulo the given m.
Take these new values and add them together to get g. You should return the
value of g modulo the given m.

Created on Mon Sep 27 07:32:01 2021

@author: gonzo
"""


# def product_except_self(nums, m):
#     """Compute the naive solution."""
#     prod_nums = 1
#     for elem in nums:
#         prod_nums *= elem

#     g = sum([prod_nums/elem % m for elem in nums]) % m

#     return g


def product_except_self(nums, m):
    """Horner's method."""
    # https://blueblazin.github.io/codefighter/commontechniques/2017/12/19/productExceptSelf.html
    s, p = 0, 1
    for num in nums:
        s, p = (p + s*num) % m, p*num % m
    return s


if __name__ == '__main__':

    # nums = [1, 2, 3, 4]
    # m = 12
    # ans = 2

    # nums = [2, 100]
    # m = 24
    # ans = 6

    # nums = [5, 8, 6, 3, 2]
    # m = 8
    # ans = 4

    # nums = [3, 3, 9, 5, 5, 4, 2, 8, 5, 9]
    # m = 17
    # ans = 16

    # nums = [27, 37, 47, 30, 17, 6, 20, 17, 21, 43, 5, 49, 49, 50, 20, 42, 45, 1, 22, 44]
    # m = 40
    # ans = 0

    # nums = [37, 50, 50, 6, 8, 54, 7, 64, 2, 64, 67, 59, 22, 73, 33, 53, 43, 77, 56, 76, 59, 96, 64, 100, 89, 38, 64, 73, 85, 96, 65, 50, 62, 4, 82, 57, 98, 61, 92, 55, 80, 53, 80, 55, 94, 9, 73, 89, 83, 80]
    # m = 67
    # ans = 55

    nums = [28, 27, 11, 17, 19, 49, 19, 46, 41, 21, 1, 49, 18, 26, 16, 24, 16, 36, 19, 49, 31, 39, 11, 21, 29, 37, 34, 34, 6, 16, 26, 31, 6, 48, 38, 36, 26, 36, 38, 18]
    m = 5040
    ans = 0

    assert product_except_self(nums, m) == ans
    print("Passed!")