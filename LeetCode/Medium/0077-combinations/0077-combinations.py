class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def walk(i, path):
            if len(path) == k:
                ans.append(path[:])
                return

            for j in range(i, n):
                path.append(j+1)
                walk(j+1, path)
                path.pop()

        walk(0, [])
        return ans