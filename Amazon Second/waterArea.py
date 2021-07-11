# import sys
#
#
# class Solution:
#     """
#     @param heights: a list of integers
#     @return: a integer
#     """
#
#     def trapRainWater(self, heights):
#         if not heights:
#             return 0
#
#         left_max = []
#         curt_max = -sys.maxsize
#         for height in heights:
#             curt_max = max(curt_max, height)
#             left_max.append(curt_max)
#
#         right_max = []
#         curt_max = -sys.maxsize
#         for height in reversed(heights):
#             curt_max = max(curt_max, height)
#             right_max.append(curt_max)
#
#         right_max = right_max[::-1]
#
#         water = 0
#         n = len(heights)
#         for i in range(n):
#             water += (min(left_max[i], right_max[i]) - heights[i])
#         return water
# solution = Solution()
# heights=[1,8,6,2,5,4,8,3,7]
# print(solution.trapRainWater(heights))
class Solution(object):
    # def maxArea(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     MAX = 0
    #     x = len(height) - 1
    #     y = 0
    #     while x != y:
    #         if height[x] > height[y]:
    #             area = height[y] * (x - y)
    #             y += 1
    #         else:
    #             area = height[x] * (x - y)
    #             x -= 1
    #         MAX = max(MAX, area)
    #     return MAX
    # O(n)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        MAX = 0
        right = len(height) - 1
        left = 0
        while right != left:
            if height[right] > height[left]:
                area = height[left] * (right - left)
                left += 1
            else:
                # area = height[right] * (left - right)
                area = height[right] * (right - left)
                right -= 1
            MAX = max(MAX, area)
        return MAX

solution = Solution()
heights=[1,8,6,2,5,4,8,3,7]
print(solution.maxArea(heights))
