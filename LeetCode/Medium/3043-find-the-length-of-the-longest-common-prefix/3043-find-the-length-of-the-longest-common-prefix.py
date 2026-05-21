class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = Trie()
        ans = 0

        for i in arr1:
            curr = root

            for j in str(i):
                if j not in curr.children:
                    curr.children[j] = Trie()
                curr = curr.children[j]

            curr.end = True

        for i in arr2:
            i = str(i)
            curr = root

            for j in range(len(i)):
                if i[j] not in curr.children:
                    ans = max(ans, j)
                    break
                curr = curr.children[i[j]]

            else:
                ans = max(ans, len(i))

        return ans

