# 用一个二维数组来存储当前位置下一个字母的index
# bcogtads
# next_pos[0][c]=1 next_pos[0][o]=2 表示b这个位置下一个最近的c的index为1，下一个最近o的index为2

def findWords(str, dict):
    if not str or not dict:
        return []
    n, ans = len(str), []
    # nextpos = [[n] * 26 for _ in range(n + 1)]
    # for i in range(n - 1, -1, -1):
    #     for j in range(26):
    #         # from back to front
    #         nextpos[i][j] = nextpos[i + 1][j]
    #         # ord(str[i])-j == ord('a') str[i]=a, j=a(0) 如果97-0=97，说明ord(str[i])==j
    #         if ord(str[i]) - ord('a') == j:
    #             nextpos[i][j] = i
    # 不断更新矩阵
    nextpos = [[n]*26 for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            nextpos[i][ord(str[j]) - ord('a')] = min(nextpos[i][ord(str[j]) - ord('a')],j)

    for word in dict:
        i, j, m = 0, 0, len(word)
        while i < n and j < m:
            # 因为包括当前位置
            i = nextpos[i][ord(word[j]) - ord('a')] + 1
            if i == n + 1:
                break
            j += 1
        if j == m:
            ans.append(word)
    return ans
str="bcogtadsjofisdhklasdj"
dict=["book","code","tag"]
print(findWords(str, dict))