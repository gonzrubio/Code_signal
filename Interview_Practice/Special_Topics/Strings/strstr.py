"""strstr().

Given two strings, text and pattern, return an integer indicating the index
in the text of the first occurrence of the pattern.
"""


def strstr(text, pattern):
    """Needle in haystack.

    Return an integer indicating the first occurrence of pattern in the text,
    or -1 if the pattern is not part of the text.
    """
    # pattern_hash = hash(pattern)
    # len_text = len(text)
    # len_pattern = len(pattern)
    # for index in range(len_text-len_pattern+1):
    #     text_hash = hash(text[index:index+len_pattern])
    #     if pattern_hash != text_hash:
    #         continue
    #     if text[index:index+len_pattern] == pattern:
    #         return index
    if not pattern or not text:
        return -1

    # First build the pattern lookup table
    tbl = [0] * (1 + len(pattern))
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            j += 1
            tbl[i] = j
        elif 0 == j:
            i += 1
        else:
            j = tbl[j]

    # Search over the query text
    i = 0
    j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if len(pattern) == j:
                assert(text[i - len(pattern): i] == pattern)
                return i - len(pattern)
        elif j == 0:
            i += 1
        else:
            j = tbl[j]
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
