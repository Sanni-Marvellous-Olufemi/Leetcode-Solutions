class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for i in range(n)]
        count = 0
        path = [[-1,0], [0, -1], [1, 0], [0, 1]]

        def walk(r, c):
            nonlocal count

            if (r >= n) or (r < 0) or (c >= n) or (c < 0) or (ans[r][c] != 0):
                return

            count += 1
            ans[r][c] = count

            while queue:
                walk(r + queue[-1][0], c + queue[-1][1])
                if queue:
                    queue.pop()


        for i in range(n):
            queue = path[:]
            walk(i, i)

        return ans
            