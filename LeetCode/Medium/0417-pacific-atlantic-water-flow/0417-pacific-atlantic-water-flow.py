class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        ans, pac, atl = [], set(), set()

        def walk(r, c, prev, ocean):
            k = (r,c)
            nonlocal row, col

            if (r >= row) or (c >= col) or (r < 0) or (c < 0) or (prev > heights[r][c]) or k in ocean:
                return 

            ocean.add(k)
            opt1 = walk(r, c+1, heights[r][c], ocean)
            opt2 = walk(r, c-1, heights[r][c], ocean)
            opt3 = walk(r-1, c, heights[r][c], ocean)
            opt4 = walk(r+1, c, heights[r][c], ocean)

            return 

        for r in range(row):
            walk(r, 0, 0, pac)
            walk(r, col-1, 0, atl)

        for c in range(col):
            walk(0, c, 0, pac)
            walk(row-1, c, 0, atl)
                    
        for i in pac:
            if i in atl:
                j, k = i
                ans.append([j,k])

        return ans

            