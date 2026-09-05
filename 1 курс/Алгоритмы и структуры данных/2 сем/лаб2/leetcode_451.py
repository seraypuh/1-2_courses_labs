class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        edge = -999999999999999
        for interval in intervals:
            if interval[0] >= edge:
                count += 1
                edge = interval[1]
        return len(intervals) - count