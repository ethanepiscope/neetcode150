# Greedy algorithm, turns out its called Kadane's algorithm. O(n) time and O(1) space

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum,current_sum)
        return max_sum
        