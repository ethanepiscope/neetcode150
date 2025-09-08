# Bit manipulation with XOR. O(n) time and O(1) space

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret ^= num
        return ret