"""Classify strings.

You categorize strings into three types: good, bad, or mixed. If a string has 3
consecutive vowels or 5 consecutive consonants, or both, then it is categorized
as bad. Otherwise it is categorized as good.

The string can also contain the character ?, which can be replaced by either
a vowel or a consonant. This means that the string "?aa" can be bad if ?
is a vowel or good if it is a consonant. This kind of string is categorized
as mixed.

Constraints: 1 ≤ |s| ≤ 50.
"""


def classifyStrings(string):
    """Return the strings category: good, bad or mixed."""
    if len(string) == 1:
        return "good"
    vowels = set("aeiou")
    vowels_mixed = set("aeiou?")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    consonants_mixed = set("bcdfghjklmnpqrstvwxyz?")

    # Can optimize to do in single pass.
    answer = "good"
    for idx in range(len(string)-2):
        set_thee = set(string[idx:idx+3])
        if set_thee.issubset(vowels):
            return "bad"
        if set_thee.issubset(vowels_mixed):
            answer = "mixed"
    for idx in range(len(string)-4):
        set_five = set(string[idx:idx+5])
        if set_five.issubset(consonants):
            return "bad"
        if set_five.issubset(consonants_mixed):
            answer = "mixed"
    for idx in range(len(string)-6):
        if set(string[idx:idx+2]).issubset(vowels) and\
           string[idx+2] == "?" and\
           set(string[idx+3:idx+7]).issubset(consonants):
            return "bad"
        if set(string[idx:idx+2]).issubset(vowels) and\
           string[idx+2] == "?" and\
           string[idx+6] == "?" and\
           set(string[idx+3:idx+6]).issubset(consonants):
            return "bad"
    return answer


def tests():
    """Sample Tests."""
    samples = [("aeu", "bad"),
               ("a?u", "mixed"),
               ("aba", "good"),
               ("a", "good"),
               ("aa", "good"),
               ("aaa", "bad"),
               ("zzzzz", "bad"),
               ("zz?zz", "mixed"),
               ("qwrtl", "bad"),
               ("qwr?l", "mixed"),
               ("???", "mixed"),
               ("?", "good"),
               ("?io", "mixed"),
               ("aa?bbbb", "bad")]
    for string, expected in samples:
        answer = classifyStrings(string)
        if answer != expected:
            print(f"string: {string}, expected: {expected}, answer: {answer}")


if __name__ == "__main__":
    tests()
