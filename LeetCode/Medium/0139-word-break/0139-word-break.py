class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sets, memo = set(wordDict), {}

        def walk(index):
            nonlocal s
            word = ""

            if index in memo:
                return memo[index]

            for i in range(index, len(s)):
                if word in sets:
                    ans = walk(i)
                    memo[i] = ans
                    if ans:
                        return True
                word += s[i]

            memo[index] = word in sets
            return memo[index]

        return walk(0)