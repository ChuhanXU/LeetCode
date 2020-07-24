# 遍历sequence，finding the first integer of sequence in array
# 如果 potential subsequence 的 index
# def isValidSubsequence(array, sequence):
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < len(array) and seqIdx < len(sequence):
#         if array[arrIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrIdx += 1
#     return seqIdx == len(sequence)
# print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0
    for value in array:
        # if seqIdx == len(sequence):
        # 	break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]))

