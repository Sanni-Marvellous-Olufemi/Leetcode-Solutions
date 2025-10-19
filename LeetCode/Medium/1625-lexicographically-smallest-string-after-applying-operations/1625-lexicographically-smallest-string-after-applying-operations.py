from heapq import heappop, heappush

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        arr1, arr2, ans = [], [], ""
        y = True if b % 2 else False

        for i in range(len(s)):
            if not y and i % 2 == 0:
                heappush(arr2, s[i])
                continue

            if a == 5:
                heappush(arr1, str(int(s[i]) % 5))
                continue

            heappush(arr1, str(int(s[i]) % 2)) if a % 2 == 0 else heappush(arr1, "0")
            

        while arr1:
            if arr2:
                ans += heappop(arr2)
            ans += heappop(arr1)

        return ans


"""
{1,3,7,9} = 0
{0,2,4,6,8} = a % 2
{5} = a % 5

"""