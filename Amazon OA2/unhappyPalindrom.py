
# input
# oldID = 'aaabbaaa'
# Output = 'aaaabaaa'
# possible strings lower alphabetically than'aaabbaaa' after one change are['aaaabaaa','aaabaaaa']
# aaaabaaa is not a palindrome and is the lowest string that can be created from oldID
# check half of the string,replace the first non 'a' character to 'a'
# if only one character, return empty string
# three case
# 'aaabbaaa'
# ''
# 'aaaaaaa'
# otherwise replace the last character to 'b'
class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome)==0:
            return ''
        for i in range(len(palindrome)):
            if palindrome[i]!='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b'
s=Solution()
Palindrome = 'aaaaaaaa'

print(s.breakPalindrome(Palindrome))