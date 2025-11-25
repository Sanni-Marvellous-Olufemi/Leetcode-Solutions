class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1

        if k == 1:
            return k

        sets = set()
        rem, curr = 1 % k, 1

        while rem not in sets:
            sets.add(rem)
            curr = (curr * 10) + 1
            rem = curr % k
    
            if rem == 0:
                return int(math.log10(curr)) + 1

        return -1
