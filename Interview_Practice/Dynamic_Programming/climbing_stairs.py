"""Climbing stairs.

Created on Sat Sep 25 14:14:59 2021

@author: gonzr

You are climbing a staircase that has n steps. You can take the steps either 1
or 2 at a time. Calculate how many distinct ways you can climb to the top of
the staircase.
"""

def climbing_stairs(n):
    if n == 1:
        return 1
    else:
        ways = 0
        one_step = 1
        two_step = 1
 
        for i in range(2, n + 1):
            ways = one_step + two_step
            one_step = two_step
            two_step = ways

        return ways
    

if __name__ == '__main__':
    # n = 4
    # n = 1
    # n = 2
    n = 13
    print(climbing_stairs(n))
