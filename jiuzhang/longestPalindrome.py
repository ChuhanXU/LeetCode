class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        length = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        hashtable = {}
        for c in s:
            if c in hashtable:
                hashtable[c] += 1
            else:
                hashtable[c] = 1

        for key, value in hashtable.items():
            if value % 2 == 0:
                length += value
                hashtable[key] = 0
            elif value // 2 > 0:
                length += (value - 1)
                hashtable[key] = 1

        for value in hashtable.values():
            if value == 1:
                length += 1
                break

        return length