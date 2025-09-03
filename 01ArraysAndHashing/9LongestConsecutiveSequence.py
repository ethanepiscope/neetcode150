#O(n^2) time. try next time to use hash set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {} #map start of sequence to end of sequence
        for num in nums: #O(n)
            if num+1 not in d.keys() and num-1 not in d.values(): #check if num cannot be added to start or end of existing sequence
                if num not in d.keys() and num not in d.values(): #assuming not, make sure num isn't a duplicate
                    d[num] = num
            if num+1 in d.keys() and num-1 in d.values(): #num is between two sequences
                for start in d.keys(): #O(n) sadly
                    if d[start] == num - 1:
                        d[start] = d[num+1]
                        del d[num+1]
                        break
            if num+1 in d.keys():
                d[num] = d[num+1]
                del d[num+1]
            if num-1 in d.values():
                for start in d.keys(): #O(n) again
                    if d[start] == num - 1:
                        d[start] = num
                        break
        ret = 0
        for start,end in d.items():
            if end-start+1 > ret:
                ret = end-start+1
        return ret