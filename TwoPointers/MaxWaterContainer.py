#O(n) time, O(1) space

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            area = (j-i)*min(heights[i],heights[j])
            if area > max_area:
                max_area = area
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        return max_area