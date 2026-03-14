class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def walk(s):
            if len(s) == n:
                ans.append(s)
                return

            for i in ["a", "b", "c"]:
                if s and i == s[-1]:
                    continue
                walk(s+i)

        walk("")
        return ans[k-1] if k <= len(ans) else ""