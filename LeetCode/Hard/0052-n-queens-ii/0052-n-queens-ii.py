class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        def walk(r, col, dia, anti):

            if r >= n:
                return 1

            count = 0
            for c in range(n):
                if (c not in col) and (r-c not in dia) and (r+c not in anti):
                    col.add(c)
                    dia.add(r-c)
                    anti.add(r+c)

                    count += walk(r+1, col, dia, anti)
                    
                    col.remove(c)
                    dia.remove(r-c)
                    anti.remove(r+c)

            return count

        return walk(0, set(), set(), set())