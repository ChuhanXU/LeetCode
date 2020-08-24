
# you can delete at most one char in the string and determine if it is a palindrome
# abca -> True
# 解题关键在于找到第一个difference
# 巧用子函数，提升代码可读性 多元组（tuple）作为函数的返回值
class Solution:
    def validPalindrome(self,s):
        if s is None:
            return False
        left,right = self.findDifference(s,0,len(s)-1)
        if left >= right:
            return True
        if self.isPalindrome(s,left+1,right) or self.isPalindrome(s,left,right-1):
            return True
        return False

    def isPalindrome(self,s,left,right):
        left,right = self.findDifference(s,left,right)
        if left >= right:
            return True
        return False


    def findDifference(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return left,right
            left += 1
            right -= 1
        return left,right

solution = Solution()
s="abcda"
print(solution.validPalindrome(s))