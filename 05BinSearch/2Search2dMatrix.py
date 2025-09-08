# O(log(m) + log(n)) time, O(1) space, where m is the number of rows and n is the number of columns in the matrix.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l < r:
            mid = (l+r+1)//2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid
        row = matrix[l]
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (l+r)//2
            if target == row[mid]:
                return True
            if target < row[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False