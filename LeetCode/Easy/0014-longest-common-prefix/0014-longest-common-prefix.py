class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = [i for i in strs[0]]
        ans = ""

        for i in strs:
            if i == strs[0]:
                continue

            curr =len(i)
            for j in range(min(len(stack), len(i))):
                if stack[j] != i[j]:
                    curr = j
                    break

            while curr < len(stack):
                stack.pop()

        return "".join(stack)