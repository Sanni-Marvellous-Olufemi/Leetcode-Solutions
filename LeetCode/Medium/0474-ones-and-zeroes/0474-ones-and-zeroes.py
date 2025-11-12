class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def walk(i, total, m, n):
            if i >= len(strs):
                return total

            counter = Counter(strs[i])
            if (counter["1"] <= n) and (counter["0"] <= m):
                opt1 = walk(i+1, total+1, m-counter["0"], n-counter["1"])
            else:
                opt1 = 0

            opt2 = walk(i+1, total, m, n)
            return max(opt1, opt2)

        return walk(0,0,m,n)