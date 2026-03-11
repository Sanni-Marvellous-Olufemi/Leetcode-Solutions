class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = ""

        for i in bin(n)[2:]:
            num += "1" if i == "0" else "0"

        return int(num, 2)