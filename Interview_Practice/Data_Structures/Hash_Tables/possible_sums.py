"""Possible sums.

You have a collection of coins, and you know the values of the coins and the
quantity of each type of coin in it. You want to know how many distinct sums
you can make from non-empty groupings of these coins.

Created on Sun Sep 26 17:15:27 2021

@author: gonzo
"""


def possible_sums(coins, quantities):
    """Brute force solution."""
    # possible_sums = set([0])
    # for coin, quantity in zip(coins, quantities):
    #     tmp = set()
    #     for possible_sum in possible_sums:
    #         for i in range(1, quantity + 1):
    #             tmp.add(possible_sum + coin * i)
    #     possible_sums.update(tmp)

    # Pythonic solution
    possible_sums = {0}
    for c, q in zip(coins, quantity):
        possible_sums = {x + c*i for x in possible_sums for i in range(q + 1)}
    return len(possible_sums) - 1


if __name__ == '__main__':

    coins = [10, 50, 100]
    quantity = [1, 2, 1]

    # coins: [10, 50, 100, 500]
    # quantity: [5, 3, 2, 2]

    # coins = [1]
    # quantity = [5]

    # coins: [1, 1]
    # quantity: [2, 3]

    # coins: [1, 2]
    # quantity: [50000, 2]

    # coins: [3, 1, 1]
    # quantity: [111, 84, 104]

    print(possible_sums(coins, quantity))
