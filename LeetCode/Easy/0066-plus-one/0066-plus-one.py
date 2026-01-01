class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        y = (len(digits) - 1)

        while y != 0 and digits[y] == 9:
            digits[y] = 0
            y -= 1

        if digits[y] == 9:
            digits[y] = 1
            digits.append(0)
            return digits
       
        digits[y] += 1
        return digits