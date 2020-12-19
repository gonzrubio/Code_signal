"""Are following patterns.

Given an array strings, determine whether it follows the sequence given in the
patterns array. In other words, there should be no i and j for which
strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which
strings[i] ≠ strings[j] and patterns[i] = patterns[j].
"""


def areFollowingPatterns(strings, patterns):
    """Return true if strings follows patterns and false otherwise.

    There should be a one-to-one correspondence between strings and patterns.
    If there isnt such correspondence then it doesnt follow the pattern.
    """
    print(set(strings))
    print(set(patterns))
    print(set(zip(strings, patterns)))
    if len(strings) == 1:
        return True

    string_dict = dict()
    pattern_dict = dict()
    for string, pattern in zip(strings, patterns):
        # New entry: new string and new pattern.
        if string not in string_dict and pattern not in pattern_dict:
            string_dict[string] = pattern
            pattern_dict[pattern] = string
            continue
        # If the string and pattern are both keys to their respective
        # hash table, then check that the string and pattern map to each other.
        if string in string_dict and string_dict[string] != pattern:
            return False
        if pattern in pattern_dict and pattern_dict[pattern] != string:
            return False
    return True


def areFollowingPatterns_efficient(strings, patterns):
    """Best solution on CodeSignal. Highlights one-to-one correspondence."""
    return len(set(strings)) == len(set(patterns)) \
        == len(set(zip(strings, patterns)))


def tests():
    """Sample Tests."""
    samples = [(["cat", "dog", "dog"], ["a", "b", "b"], True),
               (["cat", "dog", "doggy"], ["a", "b", "b"], False),
               (["cat", "dog", "dog"], ["a", "b", "c"], False),
               (["aaa", "aaa"], ["aaa", "bbb"], False),
               (["aaa"], ["aaa"], True),
               (["aaa", "aab", "aaa"], ["aaa", "aaa", "aaa"], False)]
    for strings, patterns, output in samples:
        if areFollowingPatterns(strings, patterns) != output:
            print(f"strings: {strings}, patterns: {patterns}")


if __name__ == "__main__":
    tests()
