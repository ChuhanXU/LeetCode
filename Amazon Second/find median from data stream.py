import heapq
class MedianFinder(object):

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
# [1,-2,4,6,7]
# large(4,6,7)
# small(2)
# (-1,2)
