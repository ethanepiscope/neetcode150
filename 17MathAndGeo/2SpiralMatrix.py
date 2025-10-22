# O(mn) time, O(mn) space for output array, where m and n are the dimensions of the matrix. A bit messy, took me a minute to get there.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        minrow, mincol = 0, 0
        maxrow, maxcol = len(matrix)-1, len(matrix[0])-1
        i, j = minrow, mincol
        direction = 0
        while minrow <= maxrow and mincol <= maxcol:
            ret.append(matrix[i][j])
            if direction == 0:
                if j != maxcol:
                    j += 1
                else:
                    direction = (direction+1)%4
                    i += 1
                    minrow += 1
            elif direction == 1:
                if i != maxrow:
                    i += 1
                else:
                    direction = (direction+1)%4
                    j -= 1
                    maxcol -= 1
            elif direction == 2:
                if j != mincol:
                    j -= 1
                else:
                    direction = (direction+1)%4
                    i -= 1
                    maxrow -= 1
            elif direction == 3:
                if i != minrow:
                    i -= 1
                else:
                    direction = (direction+1)%4
                    j += 1
                    mincol += 1
        return ret