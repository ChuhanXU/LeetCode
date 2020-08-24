
# 1.不断增长当前维护的字符串，判断是否在dict
# 2.遍历字典，判断前i个字符，是否与要求的字符串匹配
# input "lintcode", dict=["lint","code"]
# 输出 true
# 也可以用动态规划 word break 123
def wordBreak(s,dict):
    if s == "":
        return True
    return dfs(0,s,dict)

def dfs(start_index,s,dict):
    # 写出口
    if start_index == len(s):
        return True
    # 写拆解，遍历所有的单词，取出单词的长度
    for word in dict:
        n = len(word)
        # 如果添加该单词后index大于len(s) 或者不匹配
        if start_index + n > len(s) or s[start_index:start_index+n]!= word:
            continue
        if dfs(start_index+n,s,dict):
            return True
        return False
s =   "lintcode"
dict = ["lint","code"]
print(wordBreak(s,dict))