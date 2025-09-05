# O(n * 2^n) time, O(2^n) space for output list. took some time to figure out

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for num in nums:
            ret += [ls + [num] for ls in ret]
        return ret