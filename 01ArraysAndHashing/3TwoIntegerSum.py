# O(n) time, O(n) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals_to_idx = {}  #map a seen value to its index in nums
        for i in range(len(nums)): #O(n)
        diff = target - nums[i] #diff is the number we want in order to sum to target
            if diff in vals_to_idx: #O(1) per iter
                return [vals_to_idx[diff],i]
            vals_to_idx[nums[i]] = i #O(1) per iter


