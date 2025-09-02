# Didn't do two pointer solution here (again). O(n) time and space

class Solution:
    def trap(self, height: List[int]) -> int:
        maxPrev = [0] * len(height) #max height before index i
        maxPost = [0] * len(height)
        for i in range(1,len(height)):
            maxPrev[i] = max(maxPrev[i-1],height[i-1])
            maxPost[-i-1] = max(maxPost[-i],height[-i])
        ret = 0
        for i in range(len(height)):
            ret += max(min(maxPrev[i],maxPost[i])-height[i],0)
        return ret