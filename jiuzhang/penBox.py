# 双指针不一定要排序，因为区间和一定是递增的
# 枚举隔板
# 在隔板左边找一个最短的有效区间（双指针）N->1
# 在隔板右边找一个最短的有效区间（双指针）
# 时间复杂度N^2,要求时间复杂度为N
# 需要进行预处理
# left[i]:前i个元素的最短有效区间长度
# right[i]:第i个元素后的最短有效区间
import sys


class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    # def minimumBoxes(boxes, target):
    #     # write your code here
    #     n = len(boxes)
    #     dp = [n for _ in range(n)]
    #     right, left, sum = n - 1, n - 1, 0
    #     while left >= 0:
    #         sum += boxes[left]
    #         while sum > target:
    #             sum -= boxes[right]
    #             right -= 1
    #         while right > left and boxes[right] == 0:
    #             right -= 1
    #         if sum == target:
    #             dp[left] = right - left + 1
    #         if left + 1 < n:
    #             dp[left] = min(dp[left], dp[left + 1])
    #         left -= 1
    #     left, right, sum = 0, 0, 0
    #     ans = n + 1
    #     while right < n:
    #         sum += boxes[right]
    #         while sum > target:
    #             sum -= boxes[left]
    #             left += 1
    #         while left < right and boxes[left] == 0:
    #             left += 1
    #         if sum == target and right + 1 < n:
    #             print(left, right)
    #             ans = min(ans, right - left + 1 + dp[right + 1])
    #         right += 1
    #     if ans > n:
    #         return -1
    #     return ans
    def minimumBoxes(self,boxes, target):
        n = len(boxes)
        if n == 0:
            return -1
    # 计算左半边最短区间的数组
        left_min = self.get_minimum_valid_length(boxes,target)
    # 反转数组计算右半边最短区间数组
        boxes = boxes[::-1]
        right_min = self.get_minimum_valid_length(boxes, target)

    def get_minimum_valid_length(self,boxes,target):
    #     当前区间和
        now_sum = 0
        n = len(boxes)
        left_min = [sys.maxsize]*n
        left = 0
        for right in range(n):
            now_sum = now_sum+boxes[right]
            while now_sum>target:
                now_sum=boxes[left]
                left+=1
            if now_sum != target:
                left_min[right] = left_min[right-1]
            if now_sum == target:
                left_min[right]=min(left_min[right],right-left+1)
        return left_min





    print(minimumBoxes([1,2,2,1,1,1],3))