# O(n) time I think, O(1) space, where n is the length of nums.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0 #current index
        while cur < len(nums) - 1:
            if nums[cur] == 0:
                return False
            maxjump = nums[cur] + cur #index of max reachable number with one jump
            if maxjump >= len(nums) - 1:
                break
            nextpos = cur #accumulate index of best next number
            while cur <= maxjump:
                if cur + nums[cur] >= nextpos + nums[nextpos]:
                    nextpos = cur
                cur += 1
            cur = nextpos
        return True

        