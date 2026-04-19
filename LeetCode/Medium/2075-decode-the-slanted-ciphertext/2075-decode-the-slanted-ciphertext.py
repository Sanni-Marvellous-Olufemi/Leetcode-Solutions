class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        ans = ""

        for i in range(cols):
            r = 0
            c = i

            while r < rows and c < cols:
                index = c + (cols * r)
                ans += encodedText[index]
                r += 1
                c += 1

        return ans.rstrip()