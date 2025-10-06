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
            walk(r, c+1, heights[r][c], ocean)
            walk(r, c-1, heights[r][c], ocean)
            walk(r-1, c, heights[r][c], ocean)
            walk(r+1, c, heights[r][c], ocean)


        for r in range(row):
            walk(r, 0, 0, pac)
            walk(r, col-1, 0, atl)

        for c in range(col):
            walk(0, c, 0, pac)
            walk(row-1, c, 0, atl)
                    
        for i in pac:
            if i in atl:
                ans.append(list(i))

        return ans


"""
-You just need to recursively find all cells that can flow to each ocean then return the intersection
-Iterate through the island's borders, calling dfs on each border cell
-The parameters should be the coordinates (r,c), the previous cell and a set which tells the ocean borders cells you are currently iterating through. Call dfs with set pac (pacific) when iterating through the island's left and top edges, then use set atl (atlantic) when iterating through the  island's right and bottom edges.
-The dfs would automatically traverse the cells neighbors so add the current cell to the ocean set you passed into the function
-In the recursive function, if previous cell is greater than current cell or index is invalid or the current cell is already in the ocean set, return, Else traverse all north, south, east, and west neighbors
-If you called dfs on all border cells, the both ocean sets would have all the indices that can flow to them so return a list of both sets intersection (Indices that can flow to both oceans)
"""    