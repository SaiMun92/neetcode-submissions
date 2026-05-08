class Solution:
    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True
        
        # Make sure that is not at the edge
        if (
            row < 0 or
            col < 0 or
            row >= self.ROW or
            col >= self.COL or
            self.board[row][col] != suffix[0]
        ):
            return False
        
        # Need to make sure not to go to the same visited cell
        self.board[row][col] = "#"

        for newRow, newCol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ret = self.backtrack(row + newRow, col + newCol, suffix[1:])
            if ret:
                break
        self.board[row][col] = suffix[0]

        return ret

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROW = len(board)
        self.COL = len(board[0])
        self.board = board

        for row in range(self.ROW):
            for col in range(self.COL):
                if self.board[row][col] == word[0]:
                    if self.backtrack(row, col, word):
                        return True
        return False
