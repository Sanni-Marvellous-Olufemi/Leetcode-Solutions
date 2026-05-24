class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = {}

        def walk(i):
            if i < 0 or i >= len(arr):
                return 0

            if (len(arr) == 1) or (i == 0 and arr[i+1] >= arr[i]) or (i == len(arr)-1 and arr[i-1] >= arr[i]) or (i not in {0, len(arr)-1} and arr[i+1] >= arr[i] and arr[i-1] >= arr[i]):
                return 1
            

            if i in memo:
                return memo[i]

            ans = 0
            for j in range(d):
                idx = i+j+1
                if idx >= len(arr) or arr[idx] >= arr[i]:
                    break

                ans = max(ans, walk(idx))
            
            for j in range(d):
                idx = i-j-1
                if idx < 0 or arr[idx] >= arr[i]:
                    break

                ans = max(ans, walk(idx))

            memo[i] = ans + 1
            return ans + 1

        ans = 0
        for i in range(len(arr)):
            ans = max(ans, walk(i))

        return ans

