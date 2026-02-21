class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        def walk(i, end):
            count = 0
            curr = []

            while i <= end:
                for j in range(i, end):
                    count += 1 if s[j] == "1" else -1

                    if count == 0:
                        curr.append("1" + walk(i+1, j) + "0")
                        i = j + 1
                        break
                else:
                    i += 1
                
            curr.sort(reverse = True)
            return "".join(curr)

        return walk(0, len(s))