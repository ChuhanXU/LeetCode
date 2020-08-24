
# you are given two integer arrays a,b and one array of distinct integers c.your task is to check whether b is the longest continuous
# subarray of a consisting only of elements form c
# 3个array 判断  b 是否为 a 的最长子数组。  所有元素限定在c中
# a=[1,2,3,1,1,1]
# b=[1,2,3]
# c=[1,2,3,4]
# each of the elements of b belongs to c
# a contains b as a contiguous subarray
# b is the longest of the contiguous subarray of a which satisfy the first two conditions
# 1.先确定b是不是a的最长连续子数组
#
# # def check(a,b,c):
# #     if is_longestCA(b,a):
# #         if is_allinclude(b,c):
# #             return True
# #     return False
# def is_longestCA(b,a):
#     n = len(a)
#     length = 1
#     firstlong = 1
# def helper()
#     for i in range(n-1):
#         if a[i+1] == a[i]+1:
#             length +=1
#     return [i-length-1,i-1],length
#
#     # if length > firstlong:
#     #     index = i-(length-1)
#     #     firstlong = length
#     #     length = 1
#     # subarray = a[index:index+firstlong]
#     # return subarray
# a=[1,2,3,1,1,1]
# b=[1,2,3]
# print(a[0:3])
# print(is_longestCA(b,a))