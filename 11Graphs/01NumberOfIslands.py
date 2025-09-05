# DFS approach. O(m*n) time, where m is number of rows and n is number of columns
# O(m*n) space for the visited array and the stack

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for col in range(cols)] for row in range(rows)]
        stack = []
        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                num_islands += 1
                stack.append((i,j))
                while len(stack) != 0:
                    (i,j) = stack.pop()
                    visited[i][j] = 1
                    if i != (rows-1) and grid[i+1][j] == "1" and not visited[i+1][j]:
                        stack.append((i+1,j))
                    if i != 0 and grid[i-1][j] == "1" and not visited[i-1][j]:
                        stack.append((i-1,j))
                    if j != (cols-1) and grid[i][j+1] == "1" and not visited[i][j+1]:
                        stack.append((i,j+1))
                    if j != 0 and grid[i][j-1] == "1" and not visited[i][j-1]:
                        stack.append((i,j-1))
        return num_islands