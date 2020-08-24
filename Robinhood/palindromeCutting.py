# aaacodedoc
# 一个回文字串，需要找到以第一个字母开头的所有回文字串，将长度最长的回文字串去掉，重复操作，返回剩下的结果
# def longestPalindrome(string):
#     n = len(string)
#     if n == 0:
#         return "Empty"
#
#     longest = 0
#     for i in range(n-1):
#         for j in range(i+1,n):
#             if is_panlindrome(string,i,j):
#                 longest=max(j-i,longest)
#
#         if len(string[0:longest+1])>2:
#             string = string[longest+1::]
#             longestPalindrome(string)
#
# def is_panlindrome(string,start,end):
#     while start < end:
#         if(string[start]!=string[end]):
#             return False
#         start+=1
#         end-=1
#     return True
def palindromeCutting(string):

    palindrome = longestPalindrome(string)
    while len(palindrome)>=2:
        string = string[len(palindrome):len(string)]
        palindrome=longestPalindrome(string)
    if len(string)==0:
        return " "

def longestPalindrome(string):
    n = len(string)
    if string is None or n<=2:
        return string
    ans =''
    for i in range(1,n+1):
        if is_palindrome(string,i):
            ans = string[0:i]
    return ans


def is_palindrome(string,length):
    left = 0
    right= length-1
    while left<right:
        if string[left]!=string[right]:
            return False
        left+=1
        right -=1
    return True


print(palindromeCutting("codesignal"))

