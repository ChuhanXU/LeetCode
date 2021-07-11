import heapq


class MedianFinder(object):
    import heapq
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.large) == 0:
            heapq.heappush(self.large, num)
            return
        if num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) - len(self.small) == 2:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return -self.small[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# class MedianFinder:
# import heapq
# def __init__(self):
#     """
#     Initialize your data structure here.
#     """
#     self.small = [] # store the small half, top is the largest in the small part
#     self.large = [] # store the large half, top is the smallest in the large part

# class MedianFinder(object):
#     import heapq
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.small = []
#         self.large = []
#
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#         if len(self.large) == 0:
#             heapq.heappush(self.large, num)
#             return
#         if num >= self.large[0]:
#             heapq.heappush(self.large, num)
#         else:
#             heapq.heappush(self.small, -num)
#         if len(self.small) - len(self.large) == 2:
#             heapq.heappush(self.large, -heapq.heappop(self.small))
#
#         if len(self.large) - len(self.small) == 2:
#             heapq.heappush(self.small, -heapq.heappop(self.large))
#
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         if len(self.small) == len(self.large):
#             return (self.large[0] - self.small[0]) / 2.0
#         elif len(self.small) < len(self.large):
#             return self.large[0]
#         else:
#             return -self.small[0]