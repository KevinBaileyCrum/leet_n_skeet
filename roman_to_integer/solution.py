class Solution:
    def romanToInt(self, s: str) -> int:

        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        accum = 0
        prev = None
        for curr in reversed(s):
            if prev is not None and numerals[curr] < prev:
                accum -= numerals[curr]
            else:
                accum += numerals[curr]
            prev = numerals[curr]
        return accum

