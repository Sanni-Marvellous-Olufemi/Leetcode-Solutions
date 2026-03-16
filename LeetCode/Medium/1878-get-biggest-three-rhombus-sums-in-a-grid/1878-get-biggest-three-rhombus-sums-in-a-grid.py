from heapq import heappop, heappush

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        heap, ans = [], []

        def calc(r, c, s):
            if r + 2 * s >= m or c - s < 0 or c + s >= n:
                return 0
            
            res = 0
            
            for i, j in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
                for _ in range(s):
                    res += grid[r][c]
                    r += i
                    c += j
                    
            return res

        for r in range(m):
            for c in range(n):
                heappush(heap, -grid[r][c])
                for d in range(1, min(m, n)):
                    curr = calc(r,c,d)

                    if not curr:
                        break

                    heappush(heap, -curr)

        while heap:
            if len(ans) == 3:
                break

            curr = -heappop(heap)
            if ans and ans[-1] == curr:
                continue

            ans.append(curr)

        return ans