#O(n^2) time and space. Bitmasking approach is interesting to save O(n) space

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                entry = board[i][j]
                if entry == ".":
                    continue
                if entry in row_dict[i] or entry in col_dict[j] or entry in box_dict[(i//3,j//3)]:
                    return False
                row_dict[i].add(entry)
                col_dict[j].add(entry)
                box_dict[(i//3,j//3)].add(entry)
        return True