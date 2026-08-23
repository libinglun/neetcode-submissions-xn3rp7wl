class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda pair: pair[0])    
        newInterval = intervals[0]
        for i in range(1, len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]

            else:
                # already sorted by start point, don't have to update
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        return res
            
