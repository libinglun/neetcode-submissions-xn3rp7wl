class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals by start
        intervals.sort(key=lambda pair: pair[0])
        # if the second one overlaps with the first one, use the one that ends first
        prevEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                prevEnd = min(prevEnd, intervals[i][1])
                res += 1

        return res
