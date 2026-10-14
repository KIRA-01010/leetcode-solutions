# Roman To Integer
# Time Complexity: O(n)

class Solution(object):
    def romanToInt(self, s):
        values = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

        total = 0

        for i, ch in enumerate(s):
            if i + 1 < len(s) and values[ch] < values[s[i + 1]]:
                # subtractive case, e.g. the I in IV
                total -= values[ch]

            else:
                total += values[ch]

        return total

    # Original Idea:

    # def romanToInt(self, s):
    #     symbols = [
    #         ("IV", 4), ("IX", 9), ("XL", 40), ("XC", 90), ("CD", 400),
    #         ("CM", 900), ("I", 1), ("V", 5), ("X", 10), ("L", 50),
    #         ("C", 100), ("D", 500), ("M", 1000)
    #     ]

    #     total = 0

    #     for symbol, value in symbols:
    #         total += s.count(symbol) * value
    #         s = s.replace(symbol, "")

    #     return total