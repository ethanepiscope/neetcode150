# O(nlogn) time, O(n space), where n is the length of intervals.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        for i in range(len(intervals)-1):
            if intervals[i][1] < intervals[i+1][0]:
                ret.append(intervals[i])
            else:
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1],intervals[i+1][1])
        ret.append(intervals[-1])
        return ret