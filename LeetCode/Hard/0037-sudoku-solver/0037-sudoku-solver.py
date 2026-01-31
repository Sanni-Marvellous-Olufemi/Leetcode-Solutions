class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        col = defaultdict(set)
        sub_box = defaultdict(set)
        stack = []
        y = False

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == ".":
                    stack.append((r,c))
                    continue

                s = self.check(r, c)
                row[r].add(num)
                col[c].add(num)
                sub_box[s].add(num)


        def walk(index):
            nonlocal y

            if y: return

            r, c = stack[index]
            s = self.check(r, c)

            for i in range(1, 10):
                num = str(i)

                if num in row[r] or num in col[c] or num in sub_box[s] or y:
                    continue

                board[r][c] = num
                row[r].add(num)
                col[c].add(num)
                sub_box[s].add(num)

                if index == len(stack)-1:
                    y = True
                    return

                walk(index+1)
                row[r].remove(num)
                col[c].remove(num)
                sub_box[s].remove(num)

        if stack:
            walk(0)

    def check(self, r, c):
        if c < 3:
            c = 1
        elif c < 6:
            c = 2
        else:
            c = 3

        return ((r//3)*3) + c
            
        

        

"""
-Just Create 3 hashmaps, 1 for rows, 1 for cols and 1 for each 3 by 3 grid
-Create a helper function to calculate 3 by 3 grids
-Iterate through the board and check if the current number is in any of the hashmaps, if yes, return false, else add it to all hashmaps
-Return True
"""
        