class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0]*n for i in range(m)]
        
        for guard in guards:
            r, c = guard
            mat[r][c] = "G"
        
        for wall in walls:
            r,c = wall
            mat[r][c] = "W"
        
        path = {"l":[0,-1], "r":[0,1], "u":[-1,0], "d":[1,0]}

        def walk(r,c,p):
            nonlocal m,n
            if r in {-1, m} or c in {-1, n} or mat[r][c] in {"G", "W"}:
                return
            mat[r][c] = "g"
            walk(r + path[p][0], c + path[p][1], p)

        for guard in guards:
            r,c = guard
            walk(r-1,c,"u")
            walk(r+1,c,"d")
            walk(r,c-1,"l")
            walk(r,c+1,"r")
           
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    count += 1

        return count