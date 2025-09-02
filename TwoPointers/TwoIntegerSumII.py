#O(n) time, O(1) space. Two pointers solution

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while index1 != index2:
            total = numbers[index1] + numbers[index2]
            if total < target:
                index1 += 1
            elif total > target:
                index2 -= 1
            else:
                return [index1+1, index2+1]
        return [-1,-1]