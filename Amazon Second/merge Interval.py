class Solution(object):

    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        out = []
        out.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], intervals[i][1])
            else:
                out.append(intervals[i])
        return out