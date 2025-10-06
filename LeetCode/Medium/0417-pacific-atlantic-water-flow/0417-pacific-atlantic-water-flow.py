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
            pac.add((r,0))
            atl.add((r, col-1))
            walk(r, 1, heights[r][0], pac)
            walk(r, col-2, heights[r][col-1], atl)

        for c in range(col):
            pac.add((0, c))
            atl.add((row-1, c))
            walk(1, c, heights[0][c], pac)
            walk(row-2, c, heights[row-1][c], atl)
                    
        for i in pac:
            if i in atl:
                j, k = i
                ans.append([j,k])

        return ans

            