# str="bcogtadsjofisdhklasdj"
# dict=["book","code","tag"]
# 遍历str 将b分别和dict[0][0](b),dict[1][0](c),dict[2][0](t)比较，如果匹配上，index[j]+=1
# 创建一个index数组去记录每个单词的遍历进度
# 如果index[j]==len(dict[j]),则说明单词匹配上，将index数组的单词对应位置设置为-1，说明单词已经匹配上
# 时间复杂度为O(mn) m为单词的个数，n 为字符串长度
def findWords(str, dict):
    n = len(dict)
    index = [0] * n
    for i in range(len(str)):
        for j in range(n):
            # 若已经匹配则跳过
            if index[j] == -1:
                continue
            # 如果主串字符与子串[i]中某个目前需判断字符相同，则index[i]加一后移。
            elif dict[j][index[j]] == str[i]:
                index[j] += 1
            # 若index[j] == len(words[j])说明已经完成匹配
            if index[j] == len(dict[j]):
                index[j] = -1;
    # 遍历答案
    res = []
    for i in range(n):
        if index[i] == -1:
            res.append(dict[i])
    return res
# str="bcogtadsjofisdhklasdj"
# dict=["book","code","tag"]
# print(findWords(str, dict))
def findWords(str, dict):
    n = len(str)
    m = len(dict)
    res = []
    index = [0]*m
    for i in range(n):
        for j in range(m):
            if index[j] == -1:
                continue
            elif str[i] == dict[j][index[j]]:
                index[j]+=1
            if index[j] == len(dict[j]):
                index[j] = -1
    res = []
    for i in range(m):
        if index[i] == -1:
            res.append(dict[i])
    return res

str="bcogtadsjofisdhklasdj"
dict=["book","code","tag"]
print(findWords(str, dict))
print(ord('k')-ord('a'))


