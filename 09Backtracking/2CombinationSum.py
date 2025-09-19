# O(n^t/m) time, O(t/m) space, where n is the length of the given nums list, t is the target value and m is the minimum value.
# Used iterative backtracking to find all combinations that sum to target.
# Official solution states O(2^t/m) time, which I had trouble verifying because I couldn't figure out the 2d recurrence relation.

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        for i in range(len(nums)):
            num = nums[i]
            if target - num == 0:
                ret.append([num])
            elif target - num > 0:
                ret.extend(l+[num] for l in self.combinationSum(nums[i:],target-num))
        return ret