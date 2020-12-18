"""strstr().

Given two strings, text and pattern, return an integer indicating the index
in the text of the first occurrence of the pattern.
"""


def strstr(text, pattern):
    """Needle in haystack O(|text|) time? and O(?) space.

    Return an integer indicating the first occurrence of pattern in the text,
    or -1 if the pattern is not part of the text.
    """
    lookup = set([pattern])
    len_text = len(text)
    len_pattern = len(pattern)
    for index in range(len_text-len_pattern+1):
        if text[index:index+len_pattern] in lookup:
            return index
    return -1


def tests():
    """Sample Tests."""
    samples = [("CodesignalIsAwesome", "IA", -1),
               ("CodesignalIsAwesome", "IsA", 10),
               ("a", "a", 0),
               ("a", "A", -1),
               ("sst", "st", 1),
               ("lrnkbldxguzgcseccinlizyogwqzlifxcthdgmanjztlt", "an", 38)]
    for text, pattern, answer in samples:
        if strstr(text, pattern) != answer:
            print(f"text: {text}, pattern: {pattern}, aswer: {answer}")


if __name__ == "__main__":
    tests()


# Implement hash() with robin-algorithm/best solution in codesignal
