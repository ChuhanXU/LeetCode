
# determine if it is a palindrome string if we ignore the character case and illegal char and space
# input A man,a plan,a canal:Panama

# output True

def validPalindrome(string):
    if len(string) == 0:
        return False
    left,right = 0,len(string)-1
    while left < right:
        while left<right and not is_valid(string[left]):
            left += 1
        while left < right and not is_valid(string[right]):
            right -= 1
        if left<right and string[left].upper()!=string[right].upper():
            return False
        left += 1
        right -= 1
    return True

def is_valid(char):
    return char.isdigit()or char.isalpha()
string = "A man,a plan,a canal:Panama"
print(validPalindrome(string))