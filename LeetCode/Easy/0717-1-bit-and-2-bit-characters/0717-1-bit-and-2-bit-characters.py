class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0

        while i < len(bits):
            if i == len(bits) - 1 and bits[i] == 0:
                return True

            i += 1 if bits[i] == 0 else 2

        return False