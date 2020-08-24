
# input
# lines=[["hello", "world"],["How", "areYou", "doing"],["Please look", "and align", "to right"]]
# aligns = ["LEFT", "RIGHT", "RIGHT"]
# width = 16
def justifyNewspaperText(lines,aligns,width):


# def fullJustify(words, max_wid: int):
#     res, tmp = [], []
#     char_len = 0
#     for word in words:
#         len_word = len(word)
#         if char_len + len_word + len(tmp) - 1 >= max_wid:
#             st_res = make_str(tmp, char_len, max_wid)
#             res.append(st_res)
#             tmp, char_len = [], 0
#         tmp.append(word)
#         char_len += len_word
#     end_spaces = max_wid - char_len - len(tmp)
#     if end_spaces >= 0:
#         tmp.append(" " * end_spaces)
#     res.append(" ".join(tmp))
#     return res
#
#
# def make_str(arr, char_len, max_wid):
#     res = []
#     N = len(arr) - 1
#     spaces = [" "] * N
#     rem = max_wid - char_len - N
#     index = 0
#     while rem and spaces:
#         index = index % len(spaces)
#         spaces[index] += " "
#         index += 1
#         rem -= 1
#     for i, word in enumerate(arr):
#         res.append(word)
#         if i != N:
#             res.append(spaces[i])
#     if not spaces:
#         res.append(" " * rem)
#     return ''.join(res)
# print