"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorts = sorted(intervals, key =lambda interval : interval.start)

        for i in range(1, len(sorts)):
            i1 = sorts[i-1]
            i2 = sorts[i]

            if i1.end > i2.start:
                return False
        return True