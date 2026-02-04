class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len((board))
        col = len(board[0])

        def walk(r,c):
            nonlocal row, col

            if (c >= col) or (c < 0) or (r >= row) or (r < 0) or board[r][c] in ("X", 1):
                return

            board[r][c] = 1
            walk(r+1, c)
            walk(r-1, c)
            walk(r, c+1)
            walk(r, c-1)
            

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    if r in (0, row-1) or c in (0, col-1):
                        walk(r,c)
                        continue

                    board[r][c] = 0
                    

        for r in range(row):
            for c in range(col):
                board[r][c] = "X" if board[r][c] == 0 else board[r][c]
                board[r][c] = "O" if board[r][c] == 1 else board[r][c]
        