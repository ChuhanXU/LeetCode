# "lintcode", ["lint", "code"]
# 	输出:  true
# def wordBreak(s,dict):
#     if len(s)==0:
#         return True
#     startIndex=0
#     current=[]
#     result = []
#     return dfs(s,dict,current,startIndex,result)
# def dfs(s,dic,current,startIndex,result):
#     if startIndex==len(s):
#         result.append(current)
#         return result
#
#     for word in dic:
#         if s[startIndex:startIndex+len(word)]==word:
#             current.append(word)
#             return dfs(s,dict,current,startIndex+len(word),result)
#     return False
# dict = ["lint", "code"]
# s="lintcode"
# print(wordBreak(s,dict))
# O(2^n)
# 1 code
def wordBreak(s,dict):
    if len(s)==0:
        return True
    startIndex=0
    current=[]
    result = []
    return dfs(s,dict,current,startIndex,result)
def dfs(s,dic,current,startIndex,result):
    if startIndex==len(s):
        result.append(current)
        return result

    for word in dic:
        if s[startIndex:startIndex+len(word)]==word:
            current.append(word)
            dfs(s,dict,current,startIndex+len(word),result)
    return result
dict = ["lint", "co","we"]
s="lintde"
print(wordBreak(s,dict))


