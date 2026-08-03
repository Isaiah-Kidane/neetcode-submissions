class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val != ".":
                    if val in rows[r] or val in col[c] or val in box[(r//3,c//3)]:
                        return False
                    rows[r].add(val)
                    col[c].add(val)
                    box[(r//3,c//3)].add(val)
        return True