class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        def walk(r, c, last, path):
            if path > 3 and (r, c) != last and ((r,c) in sets):
                return True

            if grid[r][c] != grid[last[0]][last[1]]:
                return False

            visited.add((r,c))
            sets.add((r,c))
            opt1 = opt2 = opt3 = opt4 = False

            if (r, c+1) != last and (c < len(grid[0])-1):
                opt1 = walk(r, c+1, (r,c), path+1)

            if (r+1, c) != last and (r < len(grid)-1):
                opt2 = walk(r+1, c, (r,c), path+1)

            if (r, c-1) != last and (c > 0):
                opt3 = walk(r, c-1, (r,c), path+1)

            if (r-1, c) != last and (r > 0):
                opt4 = walk(r-1, c, (r,c), path+1)

            return opt1 or opt2 or opt3 or opt4


        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in visited:
                    continue
                print("")
                sets = set()
                if walk(r, c, (r, c), 0):
                    return True

        return False