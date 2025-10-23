class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2:
            dummy = ""
            for i in range(len(s)-1):
                dummy += str((int(s[i]) + int(s[i+1])) % 10)

            s = dummy

        return s[0] == s[1]