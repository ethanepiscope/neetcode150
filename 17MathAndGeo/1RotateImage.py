# O(n^2) time and O(1) space. Forgot about list.reverse(). First flip matrix vertically, then swap upper triangular entries with lower

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)//2):
            matrix[i], matrix[-i-1] = matrix[-i-1], matrix[i]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]