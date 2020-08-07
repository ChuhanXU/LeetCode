# def partition_labels(S):
#     # rightmost = {i:j for i,j in enumerate(S)}
#     # for i,j in enumerate(s) 第一个数对应每个character的index，第二个数代表具体的character,
#     # 如果想要每个字母的index，那么for前面的形式应该是 i:c 如果想要每个字母最后出现的位置就是c:i
#     # 给你一个字符串，要求你返回子串，要求这些字串彼此之间不会出现重复的字母，
#     rightmost = {c:i for i,c in enumerate(S)}
#
#     left, right = 0, 0
#
#     result = []
#     for i, letter in enumerate(S):
#
#         right = max(right, rightmost[letter])
#
#         if i == right:
#             result += [right - left + 1]
#             left = i + 1
#     return result

def partitionLabels(S):
    result = []
    rightmost = {c: i for i, c in enumerate(S)}
    #  "ababcbacadefegdehijhklij"
    # {"a":8,"b":5,"c":7 and so on}
    left = 0
    right = 0
    for i, letter in enumerate(S):
        # i = 0 letter="a" ,rightmost["a"]=8
        # 这个比较的是
        right = max(right, rightmost[letter])
        if right == i:
            result.append(right - left + 1)
            left = right + 1
    return result


print(partitionLabels("ababcbacadefegdehijhklij"))
