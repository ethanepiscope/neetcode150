#O(n^2) time, O(n)ish space for the output list.
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = set()
        for i in range(len(nums)):
            target = nums[i] * -1
            j = i + 1
            k = len(nums) - 1
            while j<k:
                total = nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    ret.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
        return list(ret)