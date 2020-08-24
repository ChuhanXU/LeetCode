
# you are given two strings pattern and s
# patterns only include 0,1
# s only include some lowercase english letters
def binaryPatternMatching(pattern,s):
    ans = 0
    n = len(pattern)
    m = len(s)
    vowels=['a','e','i','o','u','y']
    hash={}
    for i in range(m):
        if s[i] in vowels:
            hash[s[i]]=0
        else:
            hash[s[i]]=1
    for j in range(m - 3):
        i=0
        if int(pattern[0])==hash[s[j]] and int(pattern[i+1])==hash[s[j+1]] and int(pattern[i+2])==hash[s[j+2]]:
            ans+=1
        continue
    return ans

pattern = "010"
s = "amazing"
print(binaryPatternMatching(pattern,s))