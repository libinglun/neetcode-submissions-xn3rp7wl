"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # for each start time, cnt + 1, for each end time, cnt -= 1
        time = []
        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))

        # when start == end, process end (-1) before start to get minimum meeting room number
        time.sort(key = lambda x: (x[0], x[1]))
        res = 0
        count = 0
        for t in time:
            count += t[1]
            res = max(res, count)

        return res