#O(log n) time, O(1) space. Classic iterative binary search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid_idx = (l+r)//2
            if nums[mid_idx] > target:
                r = mid_idx - 1
            elif nums[mid_idx] < target:
                l = mid_idx + 1
            else:
                return mid_idx
        return -1