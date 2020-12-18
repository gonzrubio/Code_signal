"""Amend the Sentence.

Given a string s, put a single space between words and
convert uppercase letters to lowercase.
"""


def amendTheSentence(s):
    """Return the ammended sentence."""
    s = ''.join(' ' + char if char.isupper() else char.strip() for char in s)
    return s.lower().strip()


def tests():
    """Sample Tests."""
    samples = [("CodesignalIsAwesome", "codesignal is awesome"),
               ("Hello", "hello"),
               ("iEiMCyKAdsfGMPa", "i ei m cy k adsf g m pa"),
               ("kxGVMuoGggwhhsT", "kx g v muo gggwhhs t"),
               ("JklCwLha", "jkl cw lha")]
    for input_string, expected_output in samples:
        if amendTheSentence(input_string) != expected_output:
            print(input_string)


if __name__ == "__main__":
    tests()
