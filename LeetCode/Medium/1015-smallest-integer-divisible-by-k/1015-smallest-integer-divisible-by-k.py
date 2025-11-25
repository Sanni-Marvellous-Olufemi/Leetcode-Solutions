class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1

        start = "1"

        for i in range(6):
            if int(start) % k == 0:
                return len(start)

            start += "1"

        return len(start) if int(start) % k == 0 else -1