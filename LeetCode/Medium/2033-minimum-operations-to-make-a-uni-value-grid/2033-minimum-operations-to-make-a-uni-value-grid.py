class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mod = grid[0][0] % x
        curr = []
        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] % x) != mod:
                    return -1
                
                curr.append(grid[r][c])

        curr.sort()
        n = len(curr)
        
        # front, back = [0 for i in curr], [0 for i in curr]
        # for i in range(1, n):
        #     j = n - i - 1

        #     front[i] = ((curr[i] - curr[i-1]) * i) + front[i-1]
        #     back[j] = ((curr[j+1] - curr[j]) * (n-j-1)) + back[j+1]

        mid = curr[n // 2]

        for i in curr:
            ans += abs(i - mid) // x

        return ans


        