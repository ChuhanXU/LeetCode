# 背向双指针
def longestPalindromicSubstring(string):
    currentLongest = [0,1]
    for i in range(1,len(string)):
        odd = getlongest(string,i-1,i+1)
        even = getlongest(string,i-1,i)
        longest = max(odd,even,key=lambda x:x[1]-x[0])
        currentLongest=max(longest,currentLongest,key=lambda x:x[1]-x[0])
    return string[currentLongest[0]:currentLongest[1]+1]
def getlongest(string,leftIdx,rightIdx):
    while leftIdx>=0 and rightIdx<len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return[leftIdx+1,rightIdx-1]
print(longestPalindromicSubstring("abaxyzzyxf"))
string = "abaxyzzyxf"
# ba 左闭右开
print(string[1:3])
