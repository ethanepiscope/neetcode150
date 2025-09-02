# O(n) time complexity, O(n) space complexity
# Opted to return True the first time we encounter
# a duplicate instead of just comparing list and set
# lengths at the end.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #O(1)
        for num in nums: #O(n) total
            if num in seen: #O(1) per iter
                return True #O(1) per iter
            seen.add(num) #O(1) per iter
        return False #O(1)