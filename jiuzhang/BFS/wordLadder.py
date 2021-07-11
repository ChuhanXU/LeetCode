
# given two words(start and end) and a dictionary, find the shortest transformation sequence from start to end,
# output the length of sequence
# transformation rules such that:
# 1.only one letter can be changed at a time
# 2.each intermediate word must exist in the dictionary
# Input：start = "a"，end = "c"，dict =["a","b","c"]
# Output：2
# Explanation：
# "a"->"c"
# Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
# Output：5
# Explanation：
# "hit"->"hot"->"dot"->"dog"->"cog"
# import collections
#
#
import collections


def ladderLength(start,end,dict):
    n = len(dict)
    if n==0:
        return -1
    # 需要先把终点加入dict，不然到时候找不到出口
    dict.append(end)
    queue = collections.deque([start])
    visited = {}
    visited[start]=1
    while queue:
        for i in range(len(queue)):
            word = queue.popleft()
            if word == end:
                return visited[word]
            # 找到这个word所对应的一个字母转变的所有可能性，并检查这个字母是否在dict中或者是否已被visited
            wordArray = get_next_words(word)
            for next_word in wordArray:
                if next_word not in dict or next_word in visited:
                    continue
                queue.append(next_word)
                visited[next_word]=visited[word]+1
    return 0

def get_next_words(word):
    words = []
    for i in range(len(word)):
        # 先把左右两边的都拿出来，留出一个数做更改from a to z
        left,right = word[:i],word[i+1:]
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if word[i]==char:
                continue
            words.append(left+char+right)
    return words
# dict =["hot","dot","dog","lot","log"]
# print(ladderLength("hit","cog",dict))
dict =["a","b","c"]
print(ladderLength("a","c",dict))
