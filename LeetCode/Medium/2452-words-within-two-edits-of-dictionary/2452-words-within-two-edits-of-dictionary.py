class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []

        for i in queries:
            for j in dictionary:
                count = 0

                for k in range(len(i)):
                    if j[k] != i[k]:
                        count += 1

                if count <= 2:
                    ans.append(i)
                    break

        return ans