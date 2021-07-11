
# brute force
# TC:n to power three

# corner case
# are they same for capital A and lowercase a,do we have capital a in the given string
# are you guaranteed that the string is not None.
# if every character is distinct in this array can i just return the first character as the longest palindrome string

# [a,b,c,b,e]
# [a,b] [a,b,c] [a,b,c,b] [a,b,c,b,e]
# [b,c] [b,c,b] [b,c,b,e]
# method 1
# def longestPS(s):
#     if len(s)==0:
#         return ""
#     length = len(s)
#     max_len=0
#     result=""
#     for start in range(length):
#         # if don't need to return one character as longest palindrome string,we can use start instead of start+1
#         for end in range(start+1,length):
#             new_len = end-start+1
#             if new_len<=max_len:
#                 continue
#             if is_palindrome(s[start:end+1]):
#                 # print(s[start:end+1])
#                 max_len=new_len
#                 result = s[start:end+1]
#     return result
#
# def is_palindrome(s):
#     length = len(s)
#     for i in range(length//2):
#         if s[i]!=s[length-i-1]:
#             return False
#     return True
# s='abcbae'
# print(longestPS(s))

# method 2
# we can draw a conclusion according to the nature of palindrome
# we have two situations
# if the length of palin is an odd number, we can infer that the center of palindrome is a single character
# if the length of palin is an even number, we can infer that the center of palin are two same characters
# we can set two pointers at the center of this string, if the length of palin is odd number and the
# two pointers will be in the same location, otherwise, they will point at the two same center characters separately.
# repeat the same steps until the left pointer is not equal to the right pointer.
# finally we go through the total string, so the time complexity will be n squared
# from center to both ends pointers
# O(n^2)
def longestPS(s):
    if len(s)==0:
        return " "
    length = len(s)
    max_len=0
    result = ""
    for center in range(length):
        # odd situation
        start,end = center,center
        # we need to make sure start and end don't out of range

        # while valid(start,end,length):
        while start >= 0 and end < len(s):
            if s[start]!=s[end]:
                break
            new_len  = end-start+1
            if new_len>max_len:
                max_len = new_len
                result = s[start:end+1]
            start-=1
            end+=1
#         even situation
        start,end =center,center+1
        # while valid(start,end,length):

        while start >= 0 and end < len(s):
            if s[start]!=s[end]:
                break
            new_len = end-start+1
            if new_len>max_len:
                max_len=new_len
                result=s[start:end+1]
            start-=1
            end+=1
    return result
# def valid(start,end,length):
#     if start>=0 and end<=length-1:
#         return True
#     return False
s='babad'
print(longestPS(s))
