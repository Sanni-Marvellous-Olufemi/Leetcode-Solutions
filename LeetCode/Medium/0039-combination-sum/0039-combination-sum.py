class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def walk(i, curr, path):
            if i >= len(candidates) or curr > target or (curr + candidates[i]) > target:
                return

            walk(i+1, curr, path)
            dummy = []

            while curr < target:
                curr += candidates[i]
                dummy.append(candidates[i])
                walk(i+1, curr, path+dummy)

            if curr == target:
                ans.append(path+dummy)

        walk(0, 0, [])
        return ans


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(start, curr, path):
            if curr == target:
                res.append(path[:])
                return
            if curr > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if curr + num > target:
                    break
                path.append(num)
                dfs(i, curr + num, path)
                path.pop()

        dfs(0, 0, [])
        return res


