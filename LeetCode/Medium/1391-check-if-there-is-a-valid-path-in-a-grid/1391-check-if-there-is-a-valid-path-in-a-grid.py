class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        sets = set()

        def calc(num):
            ans = []
            if num == 1: ans = [[0, -1], [0, 1]]
            elif num == 2: ans = [[-1, 0], [1, 0]]
            elif num == 3: ans = [[0, -1], [1, 0]]
            elif num == 4: ans = [[0, 1], [1, 0]]
            elif num == 5: ans = [[-1, 0], [0, -1]]
            elif num == 6: ans = [[-1, 0], [0, 1]]
            return ans

        def calc2(r, c, i, j, num):
            path = calc(num)
            for dr, dc in path:
                if r + dr == i and c + dc == j:
                    for dr2, dc2 in path:
                        if r + dr2 != i or c + dc2 != j:
                            return [r + dr2, c + dc2]
                    return [r + dr, c + dc]
            return False

        def walk():
            q = deque([(0, 0)])
            sets.add((0, 0))
            
            while q:
                r, c = q.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return True
                
                num = grid[r][c]
                path = calc(num)
                
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in sets:
                        neighbor_num = grid[nr][nc]
                        if calc2(nr, nc, r, c, neighbor_num):
                            sets.add((nr, nc))
                            q.append((nr, nc))
            return False

        return walk()