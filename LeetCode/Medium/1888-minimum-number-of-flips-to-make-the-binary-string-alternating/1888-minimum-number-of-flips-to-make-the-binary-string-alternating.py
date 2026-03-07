class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s  # Double the string to handle Type-1 rotations
        
        # Two target alternating patterns
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "0" if i % 2 == 0 else "1"
            target2 += "1" if i % 2 == 0 else "0"
            
        res = float('inf')
        diff1, diff2 = 0, 0
        
        l = 0
        for r in range(len(s)):
            # Add cost for the incoming character
            if s[r] != target1[r]:
                diff1 += 1
            if s[r] != target2[r]:
                diff2 += 1
                
            # If window size > n, remove the cost for the outgoing character
            if (r - l + 1) > n:
                if s[l] != target1[l]:
                    diff1 -= 1
                if s[l] != target2[l]:
                    diff2 -= 1
                l += 1
            
            # Once we have a full window, track the minimum
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)
                
        return res


class Solution1:
    def minFlips(self, s: str) -> int:
        one = zero = 0

        for i in range(len(s)):
           one += 1 if (i % 2 == 0 and s[i] == "1") else 0
           zero += 1 if (i % 2 == 1 and s[i] == "0") else 0 

        print(zero, one)
        if len(s) % 2 == 0:
            return min(one+zero, len(s)-(one+zero))

        