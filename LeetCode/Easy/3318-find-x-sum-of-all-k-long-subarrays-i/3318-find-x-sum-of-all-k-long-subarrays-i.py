from heapq import heappop, heappush

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []

        for i in range(len(nums)-k+1):
            heap = []
            curr = nums[i:i+k]
            counter = Counter(curr)

            for key, val in counter.items():
                heappush(heap, (-val, -key))

            sums = 0
            for j in range(x):
                if heap:
                    key, val = heappop(heap)
                    key *= -1
                    val *= -1
                    sums += key *val

            ans.append(sums)

        return ans