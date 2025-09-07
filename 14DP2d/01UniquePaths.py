# bottom up DP approach. O(m*n) time and space. Solution had O(n) space by only keeping track of the lower row instead of the whole matrix.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        UP = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 or j == n-1:
                    UP[i][j] = 1
                else:
                    UP[i][j] = UP[i+1][j] + UP[i][j+1]
        return UP[0][0]