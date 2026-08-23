class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i, (s, e) in enumerate(intervals):
            # interval comes strictly before the current interval
            if newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]
            
            # interval comes strictly after the current interval
            elif newInterval[0] > e:
                res.append([s, e])          
            
            # Intervals overlap; merge them into newInterval
            else:
                newInterval = [
                    min(s, newInterval[0]), 
                    max(e, newInterval[1])
                ]
        res.append(newInterval)
        return res