class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        ans = []

        for i in nums:
            hashmap[i] += 1

        curr = sorted(hashmap.items(), key=lambda x: x[1])
        
        for i in range(k):
            j,k = curr.pop()
            ans.append(j)

        return ans