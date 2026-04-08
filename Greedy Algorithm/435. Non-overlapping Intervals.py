class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
            
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        cnt = 0
        pre_end = intervals[0][1]

        for i in range(1, n):
            start = intervals[i][0]
            end = intervals[i][1]

            if intervals[i][0] < pre_end:
                cnt += 1
            else:
                pre_end = intervals[i][1]

        return cnt
