from heapq import heappush, heappop

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = []

        for i in workerTimes:
            heappush(heap, [i, i, 2])

        while mountainHeight > 0:
            curr = heappop(heap)
            mountainHeight -= 1

            if mountainHeight == 0:
                return curr[0]

            curr[0], curr[2] = curr[0] + (curr[1] * curr[2]), curr[2] + 1
            heappush(heap, curr)


        

        