# O(mn) time, where m and n are the number of rows and columns in the grid.
# O(mn) space due to the stack (if the grid is filled with 1's).

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        stack = [] #store indices of cels to explore
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                stack.append((i,j))
                currentArea = 0
                while len(stack) > 0:
                    (i,j) = stack.pop()
                    if grid[i][j] == 1:
                        grid[i][j] = 0 #set visited
                        currentArea += 1
                    if i < rows-1 and grid[i+1][j] == 1:
                        stack.append((i+1,j))
                    if i > 0 and grid[i-1][j] == 1:
                        stack.append((i-1,j))
                    if j < cols-1 and grid[i][j+1] == 1:
                        stack.append((i,j+1))
                    if j > 0 and grid[i][j-1] == 1:
                        stack.append((i,j-1))
                maxArea = max(maxArea,currentArea)
        return maxArea