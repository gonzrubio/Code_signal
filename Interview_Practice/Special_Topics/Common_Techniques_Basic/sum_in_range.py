"""Sum in Range.

Given an array of integers nums and an array queries, where queries[i] is a
pair of indices (0-based). Find the sum of the elements in nums from the
indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add
all of the sums for all the queries together. Return the number mod 10^9 + 7.

Constraints:
1 ≤ |nums| ≤ 10^5, -10^3 ≤ nums[i] ≤ 10^3,
1 ≤ |queries| ≤ 3*10^5, |queries[i]| = 2, 0 ≤ queries[i][j] ≤ |nums| - 1,
queries[i][0] ≤ queries[i][1]

Time complexity O(|nums| + |queries|)
"""


def sumInRange(nums, queries):
    """Return the sum of all of the sums from querying nums mod 10^9 + 7."""
    cumsum = [0]*(len(nums)+1)
    for idx, elem in enumerate(nums, 1):
        cumsum[idx] = cumsum[idx - 1] + elem

    total_sum = 0
    for query in queries:
        total_sum += cumsum[query[1]+1]-cumsum[query[0]]
    return int(total_sum % (1e9+7))


def tests():
    """Sample Tests."""
    samples = [([3, 0, -2, 6, -3, 2], [[0, 2], [2, 5], [0, 5]], 10),
               ([100000], [[0, 0]], 100000),
               ([-1000], [[0, 0]], 999999007)]
    for nums, queries, expected in samples:
        output = sumInRange(nums, queries)
        if output != expected:
            print(f"nums={nums}, queries={queries}, expected={expected}\
                  output={output}")


if __name__ == "__main__":
    tests()
