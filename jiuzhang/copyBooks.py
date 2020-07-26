# 使用九章算法强化班中讲过的基于答案值域的二分法。
# 答案的范围在 max(pages)~sum(pages) 之间，每次二分到一个时间 time_limit 的时候，用贪心法从左到右扫描一下 pages，看看需要多少个人来完成抄袭。
# 如果这个值 <= k，那么意味着大家花的时间可能可以再少一些，如果 > k 则意味着人数不够，需要降低工作量。
#
# 时间复杂度 O(log(n))
# 输入: pages = [3, 2, 4], k = 2
# 输出: 5
# 解释: 第一个人复印前两本书, 耗时 5 分钟. 第二个人复印第三本书, 耗时 4 分钟.

#  是该问题时间复杂度上的最优解法
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        if not pages:
            return 0
        # 复制书籍所用的最短时间和最大时间 [3,9]
        start, end = max(pages), sum(pages)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid
        # 二分法最后剩下两个值，需要进行判断
        if self.get_least_people(pages, start) <= k:
            return start
        return end

    def get_least_people(self, pages, time_limit):
        count = 0
        time_cost = 0
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page
        #     0+3+2
        return count + 1