def compressWord(word,k):
    stack,res = [] , ''
    for x in word:
        if stack and stack[-1][0]==x:
            stack[-1][1]+=1
        else:
            stack.append([x,1])
        if stack[-1][1]==k:
            stack.pop()
    for ele , count in stack:
        res+=ele*count
    return res
word = "abbccbc"
print(compressWord(word,3))