"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]
        start.sort()
        end.sort()

        s = e = 0
        count = res = 0
        while s < len(intervals) and e < len(intervals):
            if start[s] < end[e]:
                count += 1
                res = max(count,res)
                s += 1
            else:
                count -= 1
                e += 1
        return res


        