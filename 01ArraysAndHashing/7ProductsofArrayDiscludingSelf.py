#Comments: dynamic programming :D. O(n), no usage of division operator.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preproduct = [1]*n #memoizes product of all nums up to and NOT including index i
        postproduct = [1]*n #memoizes product of all nums after and NOT including index i
        for i in range(1,n):
            preproduct[i] = preproduct[i-1] * nums[i-1]
            postproduct[-i-1] = postproduct[-i] * nums[-i]
        ret = [1]*n
        for i in range(n):
            ret[i] = preproduct[i] * postproduct[i]
        return ret
