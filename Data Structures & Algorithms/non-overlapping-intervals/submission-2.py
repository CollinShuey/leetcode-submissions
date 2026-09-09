class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevMax = intervals[0][1]
        res = 0
        for i in range(1,len(intervals)):
            if prevMax > intervals[i][0]:
                res += 1
                prevMax = min(prevMax,intervals[i][1])
                
            else:
                prevMax = max(prevMax,intervals[i][1])
        return res

        [0,2][1,3][2,4][3,5][4,6]

        