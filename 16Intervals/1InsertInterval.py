# Greedy solution. O(n) time and O(n) space for the output array

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        ret = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] < start: #disjoint  
                ret.append(interval)
            elif interval[0] > end: #disjoint        
                ret.append([start,end])
                return ret + intervals[i:]
            else:
                start = min(start,interval[0])
                end = max(end,interval[1])
        ret.append([start,end])
        return ret